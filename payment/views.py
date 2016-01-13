from django.shortcuts import render,redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse

from utilities import utility_functions

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from coupons.models import Coupon
from user_profile.models import UserProfile
from bitasync_site.models import Data_Transfer_Plan
from models import Purchase,PendingPurchase

import hashlib

from django.template import loader

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from utilities.utility_functions import generate_md5_hash

from payline_dotir.payment_gateway import send_url, get_result
from payline_dotir.settings import SEND_URL_FINAL, PAYLINE_DOTIR_API_FINAL

def gateway(request):

    amount_post = request.POST['amount']
    amount = int(amount_post)
    pending_purchase_id = generate_md5_hash(str(amount))
    redirect_url = 'http://gooshibegooshi.com/payment/result/'+pending_purchase_id+'/'

    gateway_url = send_url(amount, redirect_url,
                           SEND_URL_FINAL, PAYLINE_DOTIR_API_FINAL)
    return redirect(gateway_url)

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
def initialise_payment_payline(request,plan_name):

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

    # create a pending purchase
    pending_purchase = PendingPurchase()
    pending_purchase.data_transfer_plan = plan
    pending_purchase.user = request.user
    pending_purchase.save()

    # prepare amount
    if user_existing_coupons:
        amount = selected_plan.discounted_price
    else:
        amount =  selected_plan.original_price

    # get gateway_url
    # integrate pending purchase hashcode in redirect url
    redirect_url = 'http://gooshibegooshi.com/payment/result_payline/'+pending_purchase.hashcode+'/'
    gateway_url = send_url(amount, redirect_url,SEND_URL_FINAL, PAYLINE_DOTIR_API_FINAL)

    # redirect to payline.ir
    return redirect(gateway_url)


@csrf_exempt
def result_payline(request,pending_purchase_hashcode):


    trans_id = request.POST['trans_id']
    id_get = request.POST['id_get']
    final_result = get_result(PAYLINE_DOTIR_API_FINAL, trans_id, id_get)

    if int(final_result) == 1:
        # inset the purchase into database, and remove pending purchase
        pay_for_a_plan_complete(pending_purchase_hashcode)
    else:
        # remove pending purchase
        return HttpResponse("payment failed")


def pay_for_a_plan_complete(pending_purchase_hashcode):

    context = {}

    return HttpResponse("your plan is now activated")


    # retrieve the pending purchase
    pending_purchase = PendingPurchase.objects.get(hashcode = pending_purchase_hashcode)

    # get the user's coupons
    user_profile = UserProfile.objects.get( user = pending_purchase.user )
    user_existing_coupons = Coupon.objects.filter( user_profile = user_profile )

    # create the temp plan for the plan selected by user
    selected_plan = utility_functions.create_temp_plan(pending_purchase.data_transfer_plan, user_existing_coupons)
    #context['selected_plan'] = selected_plan

    # does the user have any coupons?
    #if not user_existing_coupons:
    #    context['coupon_available'] = False

    #else:
                # if the customer has some coupons
    #    context['coupon_available'] = True
    #    context['existing_coupons'] = user_existing_coupons
        # get the best coupon



    # add the purchase to the database
    new_purchase = Purchase()
    new_purchase.user = pending_purchase.user
    new_purchase.data_transfer_plan = pending_purchase.data_transfer_plan

    if user_existing_coupons:
        new_purchase.amount_paid = selected_plan.discounted_price
    else:
        new_purchase.amount_paid = selected_plan.original_price

    new_purchase.save()
    # save follow_up number using hash

    follow_up_number = generate_md5_hash(str(new_purchase.id))
    new_purchase.follow_up_number = follow_up_number
    new_purchase.save()

    context['follow_up_number'] = follow_up_number

    # if necessary, remove user's best coupon
    if user_existing_coupons:
        best_coupon = utility_functions.get_best_coupon(user_existing_coupons)
        best_coupon.delete()

    # remove pending purchase
    pending_purchase.delete()

    # send an email
    plaintext = loader.get_template('payment/pay_for_a_plan_complete_email.txt')
    htmly = loader.get_template('payment/pay_for_a_plan_complete_email.html')
    subject = loader.get_template('payment/pay_for_a_plan_complete_email_subject.html')

    subject_content = subject.render(context).replace('\n',' ')
    text_content = plaintext.render(context)
    html_content = htmly.render(context)

    from_email = 'sales@gooshibegooshi.com'
    recipient_list = [new_purchase.user.email]

    msg = EmailMultiAlternatives(subject_content, text_content, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    # return response to the user.
