from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user_profile.models import UserProfile, CustomerProfile

from .models import B2C_Coupon
from .forms import AddGiftCardForm 



# Create your views here.

@login_required
def add_coupon_to_profile(request): 

    if request.method == 'POST': 
    
        # validate the card
        form = AddGiftCardForm(request.POST)
        
        if form.is_valid():
         
            hashcode = form.cleaned_data['hashcode']
           
            # associate the code to the customer profile 
            user_profile = UserProfile.objects.get( user=request.user )
            customer_profile = CustomerProfile.objects.get( user_profile=user_profile )
           
            try: 
                b2c_coupon = B2C_Coupon.objects.get(hashcode = hashcode)
                b2c_coupon.customer_profile = customer_profile
                b2c_coupon.save()          
           
                return HttpResponseRedirect("/coupons/add_b2c_coupon_success/"+hashcode+"/")

            except B2C_Coupon.DoesNotExist:
                return HttpResponseRedirect("/coupons/add_b2c_coupon_failure/")
                
           
        else: 

            context = {}
            context.update(csrf(request))

            # get the list of existing coupon for the customer
            user_profile = UserProfile.objects.get( user=request.user )
            customer_profile = CustomerProfile.objects.get( user_profile=user_profile )
            b2c_coupons = B2C_Coupon.objects.filter(customer_profile = customer_profile)
            context['existing_coupons'] = b2c_coupons
                    
            context['form'] = form 

            #todo: put a capcha verifier in this form. 
            return render(request,'coupons/add_gift_card.html',context)
        
        
    else: 

        context = {}
        context.update(csrf(request))

        # get the list of existing coupon for the customer
        user_profile = UserProfile.objects.get( user=request.user )
        customer_profile = CustomerProfile.objects.get( user_profile=user_profile )
        b2c_coupons = B2C_Coupon.objects.filter(customer_profile = customer_profile)
        context['existing_coupons'] = b2c_coupons
                
        # the form for adding new b2c coupons 
        form = AddGiftCardForm()
        context['form'] = form 
        
        return render(request,'coupons/add_gift_card.html',context)
        
def add_b2c_coupon_success(request,hashcode): 
    return HttpResponse("You have successfully added your gift card")  


def add_b2c_coupon_failure(request): 
    return HttpResponse("Your gift card code is not valid")  

