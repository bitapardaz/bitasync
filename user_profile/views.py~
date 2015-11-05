from django.shortcuts import render

from django.template.context_processors import csrf
from django.template import RequestContext, loader

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .models import ShopProfile
from .models import CustomerProfile

from .forms import UserProfileForm
from .forms import MyProfileCustomerForm
from .forms import MyProfileShopForm

   
@login_required    
def myprofile(request): 

    if request.method == 'POST' : 
        pass 
        
    else: 
    
        args = {}
        args.update(csrf(request))
    
        #user = User.objects.get(username=request.user.username)
        user_profile = UserProfile.objects.get(user=request.user)
    
        # depending on the type of the user, the template will respond differently. 
        args['is_shop'] = user_profile.is_shop
        
        if user_profile.is_shop: 
            args['shop_details_form'] = MyProfileShopForm()
        else: 
            args['customer_details_form'] = MyProfileCustomerForm()

        
    
        template = loader.get_template('user_profile/myprofile.html')
        context = RequestContext(request,args)
        return HttpResponse(template.render(context))    

    return HttpResponse("Your profile") 
    
def register(request):

    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, prefix='user')
        user_profile_form = UserProfileForm(request.POST, prefix = 'userprofile')             
             
        if user_form.is_valid() & user_profile_form.is_valid():
            
            
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']         
            email = user_profile_form.cleaned_data['email']
            
            user = User.objects.create_user(username=username, password=password, email=email)

#           user = user_form.save()             
#            user.save()
                        
            user_profile = UserProfile()        
            user_profile.user = user
            
            user_profile.is_shop = user_profile_form.cleaned_data['is_shop']
            #user_profile.email_subscription = user_profile_form.cleaned_data['email_subscription']
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
            
            return HttpResponse(email)
            #return HttpResponseRedirect("/accounts/register_success")
         
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
 
