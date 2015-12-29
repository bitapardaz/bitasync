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

            is_generated = create_bulk_license(shop_username,license_type,copies)

            if is_generated:
                return HttpResponseRedirect('/shop_billing/bulk_license_create_done/'+
                                        shop_username + '/' +
                                        license_type + '/' +
                                        str(copies) + '/'
                                       )
            else:
                return HttpResponse("Failed to generate licenses in bulk. Try again.")

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
    return True


#@login_required
#def bulk_license_select_shop(request):

#    if request.method == 'POST':

#            if 'find_shop' in request.POST:

#                select_shop_form = GetUserNameForm(request.POST)
#                generate_bulk_license_form = GenerateBulkLicenseForm(custom_choices=[])

#                if select_shop_form.is_valid():
                    # get the username from text box
                    # initialise the data that gets into the dropbox
#                    fusername = select_shop_form.cleaned_data['username']
#                    shop_profiles = ShopProfile.objects.filter(
#                        user_profile__user__username__contains=fusername)

#                    usernames = [(shop_profile.user_profile.user.username,
#                                  shop_profile.user_profile.user.username)
#                                 for shop_profile in shop_profiles]

#                    import pdb; pdb.set_trace()
                    # set the usernames found as initial values for next choice

#                    generate_bulk_license_form = GenerateBulkLicenseForm(custom_choices=usernames)
#                    import pdb; pdb.set_trace()


#            if 'generate_license' in request.POST:
#                import pdb; pdb.set_trace()


#                generate_bulk_license_form = GenerateBulkLicenseForm(request.POST)
#

                #import pdb; pdb.set_trace()

#                if generate_bulk_license_form.is_valid():
#                    shop_username = generate_bulk_license_form.cleaned_data['shop_id']
#                    license_type = generate_bulk_license_form.cleaned_data['license_type']
#                    copies = generate_bulk_license_form.cleaned_data['copies']

                    # create the bulk license and put them in the database
                    #generate_and_store_bulk_license(shop_username,
                    #                                license_type,
                    #                                copies)


                #import pdb; pdb.set_trace()

#    else:
        # get the list of all shops
        # initialise an empty dropbox
        # put it in the context
#        shop_profiles = []
#        select_shop_form = GetUserNameForm()
#        generate_bulk_license_form = GenerateBulkLicenseForm(custom_choices=[])

#    context = {}

#    context.update(csrf(request))

#    select_shop_form = GetUserNameForm()
#    context['select_shop_form'] = select_shop_form
#    context['generate_bulk_license_form'] = generate_bulk_license_form

#    return render(request, 'shop_billing/bulk_license_select_shop.html',
#                  context)


#def generate_and_store_bulk_license(shop_username, license_type, copies):
#    pass
