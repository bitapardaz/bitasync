from django.shortcuts import render

from django.template.context_processors import csrf
from django.template import RequestContext, loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

from .models import UserProfile
from .models import ShopProfile
from .models import CustomerProfile

from .forms import UserProfileForm
from .forms import MyProfileCustomerForm
from .forms import MyProfileShopForm

from django.core.mail import send_mail


def my_password_reset(request): 
    # calls django.contrib.auth.views.password_reset with its customisations 
    # and returns the result
    response = auth_views.password_reset(request,
                                         template_name='user_profile/password_reset.html',
                                         post_reset_redirect='/accounts/password_reset_done',
                                         from_email='passwords@bitasync.com',
                                         current_app='user_profile')
    return response
    
    
def my_password_reset_done(request): 
    return HttpResponse('Please check your email')
    
def my_password_reset_confirm(request,uidb64,token): 
    response = auth_views.password_reset_confirm(request,
                                                 uidb64=uidb64,
                                                 token=token,
                                                 template_name='user_profile/password_reset_confirm.html',
                                                 post_reset_redirect='/accounts/password_reset_complete',
                                                 current_app='user_profile')
                                                 
    return response                                                 
   
   
def my_password_reset_complete(request): 

    response = """
                Password Change Complete. 
                <hr>
                Click <a href="/accounts/login"> here </a> to login.
                """
    return HttpResponse(response)


@login_required
def my_password_change_done(request): 

    template_name = 'user_profile/password_change_done.html'
    
    response = auth_views.password_change_done(request,template_name=template_name)
    
    # send email to notify the user that his password has changed. 
    subject = 'Password Change'
    message = 'Your password was succcessfully changed.'
    from_email = 'passwords@bitasync.com'
    recipient_list = [request.user.email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list,fail_silently=False)  
    
    return response

    

@login_required    
def myprofile(request): 

    if request.method == 'POST' : 
        
        user_profile = UserProfile.objects.get(user=request.user)
         
        if user_profile.is_shop:                    
            shop_profile_form = MyProfileShopForm(request.POST)
            if shop_profile_form.is_valid():
             
                if shop_profile_form.has_changed():
                    
                    # get the data out of the forms.
                    email = shop_profile_form.cleaned_data['email']
                    mobile = shop_profile_form.cleaned_data['mobile']
                    email_subscription = shop_profile_form.cleaned_data['email_subscription']
                    address = shop_profile_form.cleaned_data['address']
                    landline = shop_profile_form.cleaned_data['landline']
                    bank_card_number = shop_profile_form.cleaned_data['bank_card_number']
                    account_holder = shop_profile_form.cleaned_data['account_holder']
                    
                    # save the data into the database
                    user_profile = UserProfile.objects.get(user=request.user)   
                    shop_profile = ShopProfile.objects.get(user_profile=user_profile)

                    request.user.email = email
                    
                    user_profile.mobile = mobile
                    user_profile.email_subscription = email_subscription
                    
                    shop_profile.address = address 
                    shop_profile.landline = landline
                    shop_profile.bank_card_number = bank_card_number
                    shop_profile.account_holder = account_holder
                    
                    request.user.save()
                    user_profile.save()
                    shop_profile.save()
                    
                    return HttpResponseRedirect('/accounts/myprofile/')

            
            else: 
                # user_profile form is not valid
                return HttpResponse("error: submited form is not valid.")
            
        else: 
            # user is not a shop
             
            customer_profile_form = MyProfileCustomerForm(request.POST)
            if customer_profile_form.is_valid():      
                if customer_profile_form.has_changed():
                
                    # get the data out of the form 
                    email = customer_profile_form.cleaned_data['email']
                    mobile = customer_profile_form.cleaned_data['mobile']
                    email_subscription = customer_profile_form.cleaned_data['email_subscription']                   
                    
                    # save it to the database. 
                    user_profile = UserProfile.objects.get(user=request.user)                    
                    request.user.email = email
                    user_profile.mobile = mobile
                    user_profile.email_subscription = email_subscription
                    user_profile.save()
                    request.user.save()
                    
                    return HttpResponseRedirect('/accounts/myprofile/')
            
                
                else: 
                    # the form has not changed. Do nothing. 
                    # redirect to homepage?    
                    return HttpResponseRedirect('/accounts/myprofile/')          
            else: 
                # todo
                # the form is not valid. 
                # return the form to the user.
                pass 
        
    else: 
        # if the request does not have POST method
        args = {}
        args.update(csrf(request))
    
        #user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(user=request.user)
        
        data = {}
            
        data['email'] = request.user.email
        data['mobile'] = user_profile.mobile 
        data['email_subscription'] = user_profile.email_subscription
        
        # depending on the type of the user, the template will respond differently. 
        args['is_shop'] = user_profile.is_shop
        
        if user_profile.is_shop:                    
        
            shop_profile = ShopProfile.objects.get(user_profile = user_profile)
            data['address'] = shop_profile.address
            data['landline'] = shop_profile.landline
            data['reward'] = shop_profile.reward
            data['bank_card_number'] = shop_profile.bank_card_number
            data['account_holder'] = shop_profile.account_holder
            
        
            args['shop_details_form'] = MyProfileShopForm(initial=data)
            
        else: 
            # if the customer is a normal customer.
            # no additional iterms are added to data. 
            args['customer_details_form'] = MyProfileCustomerForm(initial=data)

    
        template = loader.get_template('user_profile/myprofile.html')
        context = RequestContext(request,args)
        return HttpResponse(template.render(context))    


    
def register(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user')
        user_profile_form = UserProfileForm(request.POST, prefix = 'userprofile')             
             
        if user_form.is_valid() & user_profile_form.is_valid():
            
            
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']         
            email = user_profile_form.cleaned_data['email']
            
            user = User.objects.create_user(username=username, password=password, email=email)
                       
            user_profile = UserProfile()        
            user_profile.user = user
            
            user_profile.is_shop = user_profile_form.cleaned_data['is_shop']
            user_profile.email_subscription = True
            user_profile.mobile = user_profile_form.cleaned_data['mobile']  
                                   
            user_profile.save()
            
            if user_profile.is_shop: 
                # if the user represents a shop
                shop_profile = ShopProfile()
                shop_profile.user_profile = user_profile
                shop_profile.address = user_profile_form.cleaned_data['address']
                shop_profile.save()
                

            else: 
                # if the user represents a normal customer (as opposed to a shop) 
                customer_profile = CustomerProfile()
                customer_profile.user_profile = user_profile
                customer_profile.save()
            

            return HttpResponseRedirect("/accounts/register_success")
         
        else: 
            return HttpResponse('There was an error on the registration form submitted.')     
       
    else: 
    
        user_form = UserCreationForm(prefix='user')
        user_profile_form = UserProfileForm(prefix='userprofile')
        
        args= {}
        args.update(csrf(request))
        args['user_form'] = user_form
        args['user_profile_form'] = user_profile_form
        
        template = loader.get_template('user_profile/registration.html')
        context = RequestContext(request,args)
        return HttpResponse(template.render(context))
         
       
def login(request):
        c = {}
        c.update(csrf(request))
        template = loader.get_template('user_profile/login.html')
        context = RequestContext(request, c)
        return HttpResponse(template.render(context))


def logout(request):
    auth.logout(request)
    template = loader.get_template('user_profile/loggedout.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def auth_view(request):
    # this view only performs an action based on the authentication form.
    # therefore, it does not need a template
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

      
def my_login(request): 

    response = auth_views.login(request,
                                template_name="user_profile/my_login.html", 
                                )
    
    return response 

    

def loggedin(request):
    template = loader.get_template('user_profile/loggedin.html')
    name = request.user.username
    context = RequestContext(request, {'fullname': name})
    return HttpResponse(template.render(context))


def invalid(request):
    template = loader.get_template('user_profile/invalid.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))
    
 
     
def register_success(request): 

        template = loader.get_template('user_profile/registration_success.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))
 
