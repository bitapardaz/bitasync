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


@login_required
def bulk_license_select_shop(request):

    if request.method == 'POST':

            if 'find_shop' in request.POST:

                select_shop_form = GetUserNameForm(request.POST)

                if select_shop_form.is_valid():
                    # get the username from text box
                    # initialise the data that gets into the dropbox
                    fusername = select_shop_form.cleaned_data['username']
                    shop_profiles = ShopProfile.objects.filter(
                        user_profile__user__username__contains=fusername)

                    usernames = [(shop_profile.user_profile.user.username,
                                  shop_profile.user_profile.user.username)
                                 for shop_profile in shop_profiles]

                    # set the usernames found as initial values for next choice

                    generate_bulk_license_form = GenerateBulkLicenseForm(choices=usernames)

            if 'generate_license' in request.POST:

                
                generate_bulk_license_form = GenerateBulkLicenseForm(request.POST)


                if generate_bulk_license_form.is_valid():
                    shop_username = generate_bulk_license_form.cleaned_data['shop_id']
                    license_type = generate_bulk_license_form.cleaned_data['license_type']
                    copies = generate_bulk_license_form.cleaned_data['copies']

                    # create the bulk license and put them in the database
                    #generate_and_store_bulk_license(shop_username,
                    #                                license_type,
                    #                                copies)
                select_shop_form = GetUserNameForm()

    else:
        # get the list of all shops
        # initialise an empty dropbox
        # put it in the context
        shop_profiles = []
        select_shop_form = GetUserNameForm()
        generate_bulk_license_form = GenerateBulkLicenseForm(choices=[])

    context = {}
    context.update(csrf(request))
    context['select_shop_form'] = select_shop_form
    context['generate_bulk_license_form'] = generate_bulk_license_form

    return render(request, 'shop_billing/bulk_license_select_shop.html',
                  context)


def generate_and_store_bulk_license(shop_username, license_type, copies):
    pass
