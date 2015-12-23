from django.shortcuts import render
from django.template.context_processors import csrf

from django.http import HttpResponse

from utilities import utility_functions

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from coupons.models import Coupon
from user_profile.models import UserProfile
from bitasync_site.models import Data_Transfer_Plan
from models import Purchase

import hashlib

from django.template import loader

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

@login_required
def pay_for_a_plan(request,plan_name):

    context = {}

    #check if the plan is valid.
    valid_plans = ["L1","L2","L5","U1","U3","U6"]
    if plan_name not in valid_plans :
        raise Http404("Data transfer selected is not valid.")

    # get the plan the user has selected
    all_plans = Data_Transfer_Plan.objects.all()
    plan = utility_functions.get_plan_by_name(all_plans,plan_name)

    # get the user's coupons
    user_profile = UserProfile.objects.get( user = request.user )
    user_existing_coupons = Coupon.objects.filter( user_profile = user_profile )

    # create the temp plan for the plan selected by user
    selected_plan = utility_functions.create_temp_plan(plan, user_existing_coupons)
    context['selected_plan'] = selected_plan

    # does the user have any coupons?
    if not user_existing_coupons:
        context['coupon_available'] = False

    else:
                # if the customer has some coupons
        context['coupon_available'] = True
        context['existing_coupons'] = user_existing_coupons

        # get the best coupon
        best_coupon = utility_functions.get_best_coupon(user_existing_coupons)


    return render(request,'payment/pay_for_a_plan.html',context)

@login_required
def pay_for_a_plan_complete(request,plan_name,token):

    context = {}

    #check if the plan is valid.
    valid_plans = ["L1","L2","L5","U1","U3","U6"]
    if plan_name not in valid_plans :
        raise Http404("Data transfer selected is not valid.")

    # get the plan the user has selected
    all_plans = Data_Transfer_Plan.objects.all()
    plan = utility_functions.get_plan_by_name(all_plans,plan_name)

    # get the user's coupons
    user_profile = UserProfile.objects.get( user = request.user )
    user_existing_coupons = Coupon.objects.filter( user_profile = user_profile )

    # create the temp plan for the plan selected by user
    selected_plan = utility_functions.create_temp_plan(plan, user_existing_coupons)
    context['selected_plan'] = selected_plan

    # does the user have any coupons?
    if not user_existing_coupons:
        context['coupon_available'] = False

    else:
                # if the customer has some coupons
        context['coupon_available'] = True
        context['existing_coupons'] = user_existing_coupons
        # get the best coupon
        best_coupon = utility_functions.get_best_coupon(user_existing_coupons)

    # add the purchase to the database
    new_purchase = Purchase()
    new_purchase.user = request.user
    new_purchase.data_transfer_plan = plan

    if user_existing_coupons:
        new_purchase.amount_paid = selected_plan.discounted_price
    else:
        new_purchase.amount_paid = selected_plan.original_price

    # save follow_up number using hash
    hasher = hashlib.md5()
    hasher.update(str(new_purchase.id))
    follow_up_number = hasher.hexdigest()
    new_purchase.follow_up_number = follow_up_number
    new_purchase.save()
    context['follow_up_number'] = follow_up_number

    # if necessary, remove user's best coupon
    if user_existing_coupons:
        best_coupon.delete()

    # send an email
    plaintext = loader.get_template('payment/pay_for_a_plan_complete_email.txt')
    htmly = loader.get_template('payment/pay_for_a_plan_complete_email.html')
    subject = loader.get_template('payment/pay_for_a_plan_complete_email_subject.html')


    subject_content = subject.render(context).replace('\n',' ')
    text_content = plaintext.render(context)
    html_content = htmly.render(context)

    from_email = 'sales@gooshibegooshi.com'
    recipient_list = [request.user.email]

    msg = EmailMultiAlternatives(subject_content, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return HttpResponse("your plan is now activated")
