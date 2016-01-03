from django.shortcuts import render
from django.template.context_processors import csrf
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from forms import GetUserNameForm, GenerateBulkLicenseForm

from user_profile.models import ShopProfile
from models import BulkLicenseManagement

from django.db import DatabaseError
from utilities.utility_functions import generate_md5_hash

from user_profile.models import UserProfile,CustomerProfile

from payment.models import Purchase
from bitasync_site.models import Data_Transfer_Plan

from tasks import generate_license_pdf_files


@login_required
def bulk_created_done(request,shop_username,plan_name,copies):
    output = "Successfully generated " + copies + " of license type " + plan_name + " for shop with id: " + shop_username
    return HttpResponse(output)


@login_required
def bulk_license_input_shop_username(request):

    if request.method == "POST":

        input_shop_fusername_form = GetUserNameForm(request.POST)

        if input_shop_fusername_form.is_valid():
            fusername = input_shop_fusername_form.cleaned_data['username']
            return HttpResponseRedirect('/shop_billing/bulk_license_create/'+ fusername +'/')

    else:
            input_shop_fusername_form = GetUserNameForm()


    context={}
    context['input_shop_fusername_form'] = input_shop_fusername_form

    return render(request, 'shop_billing/bulk_license_input_shop.html',
                  context)



@login_required
def bulk_license_create(request,fusername):

    if request.method=="POST":

        shop_profiles = ShopProfile.objects.filter(
        user_profile__user__username__contains=fusername)

        usernames = [(shop_profile.user_profile.user.username,
            shop_profile.user_profile.user.username)
            for shop_profile in shop_profiles]

        generate_bulk_license_form = GenerateBulkLicenseForm(usernames,request.POST)

        if generate_bulk_license_form.is_valid():

            shop_username = generate_bulk_license_form.cleaned_data['shop_id']
            license_type = generate_bulk_license_form.cleaned_data['license_type']
            copies = generate_bulk_license_form.cleaned_data['copies']

            try:
                create_bulk_license(shop_username,license_type,copies)

            except DatabaseError:
                return HttpResponse("Concurrent access to bulk license management system prohibited. Try again.")

            else:
                return HttpResponseRedirect('/shop_billing/bulk_license_create_done/'+
                                        shop_username + '/' +
                                        license_type + '/' +
                                        str(copies) + '/'
                                       )


    else:

        shop_profiles = ShopProfile.objects.filter(
            user_profile__user__username__contains=fusername)

        usernames = [(shop_profile.user_profile.user.username,
            shop_profile.user_profile.user.username)
            for shop_profile in shop_profiles]

        generate_bulk_license_form = GenerateBulkLicenseForm(all_usernames = usernames)

    context = {}
    context['generate_bulk_license_form'] = generate_bulk_license_form

    data = {}
    data['username'] = fusername
    input_shop_fusername_form = GetUserNameForm(initial=data)
    context['input_shop_fusername_form'] = input_shop_fusername_form

    return render(request,'shop_billing/bulk_license_create.html',context)


def create_bulk_license(shop_username,plan_name,copies):

    prefix = BulkLicenseManagement.objects.all()[0].bulk_license_username_prefix
    data_transfer_plan = Data_Transfer_Plan.objects.get(plan_name=plan_name)
    selling_shop = User.objects.get(username = shop_username)

    user_pass_collection = []

    for copy_index in range(0,copies):
        (username,password) = create_one_license(selling_shop,data_transfer_plan,prefix)
        user_pass_collection.append((username,password))

    # run the generation of license pdf files as a async task using celery
    generate_license_pdf_files.delay(user_pass_collection)

def create_one_license(selling_shop,data_transfer_plan,prefix):
    # read current index
    bulk_license_manager = BulkLicenseManagement.objects.all()[0]
    current_index = bulk_license_manager.current_index

    # set up username and password
    username = prefix + str(current_index)
    password = generate_md5_hash(selling_shop.username + str(current_index))
    new_user = User(username=username, password=password)

    current_index2 = BulkLicenseManagement.objects.all()[0].current_index
    if current_index != current_index2:
        raise DatabaseError()

    else:
        new_user = User.objects.create_user(username=username, password=password)

        # create a userprofile for the new customer
        new_user_profile = UserProfile()
        new_user_profile.user = new_user
        new_user_profile.is_shop = False
        new_user_profile.email_subscription = False
        new_user_profile.save()

        # create CustomerProfile
        new_customer_profile = CustomerProfile()
        new_customer_profile.user_profile = new_user_profile
        new_customer_profile.save()

        #create purchase object
        new_purchase = Purchase()
        new_purchase.user = new_user
        new_purchase.data_transfer_plan = data_transfer_plan
        new_purchase.remaining_allowance_frequency = data_transfer_plan.freq
        new_purchase.selling_shop = selling_shop
        # purchase.shop_debited = false is by default.

        new_purchase.save()
        new_purchase.follow_up_number = generate_md5_hash(str(new_purchase.id))

        new_purchase.save()

        #increase the current index
        current_index = current_index + 1
        bulk_license_manager.current_index = current_index
        bulk_license_manager.save()

        return (username,password)
