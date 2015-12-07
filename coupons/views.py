from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from user_profile.models import UserProfile, CustomerProfile

from .models import Coupon
from .forms import AddGiftCardForm 

from bitasync_site.models import Data_Transfer_Plan

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
            
            try: 
                coupon = Coupon.objects.get(hashcode = hashcode)
                coupon.user_profile = user_profile
                coupon.save()          
           
                return HttpResponseRedirect("/coupons/add_coupon_success/"+hashcode+"/"+str(coupon.discount_rate)+"/")

            except Coupon.DoesNotExist:
                return HttpResponseRedirect("/coupons/add_coupon_failure/")
                
           
        else: 

            context = {}
            context.update(csrf(request))

            # get the list of existing coupon for the customer
            user_profile = UserProfile.objects.get( user=request.user )
            coupons = Coupon.objects.filter(user_profile = user_profile)
            context['existing_coupons'] = coupons
                    
            context['form'] = form 

            #todo: put a capcha verifier in this form. 
            return render(request,'coupons/add_coupon.html',context)
        
        
    else: 

        context = {}
        context.update(csrf(request))

        # get the list of existing coupon for the customer
        user_profile = UserProfile.objects.get( user=request.user ) 
        coupons = Coupon.objects.filter(user_profile = user_profile)
        context['existing_coupons'] = coupons
                
        # the form for adding new b2c coupons 
        form = AddGiftCardForm()
        context['form'] = form 
        
        return render(request,'coupons/add_coupon.html',context)
        
def add_coupon_success(request,hashcode,discount_rate): 

    context={}
    context['discount_percentage'] = int(float(discount_rate) * 100)
    
    # get original prices from database
    original_price_L1 = Data_Transfer_Plan.objects.get(plan_name="L1").price
    original_price_L3 = Data_Transfer_Plan.objects.get(plan_name="L3").price
    original_price_L6 = Data_Transfer_Plan.objects.get(plan_name="L6").price
    
    # original prices for L1, L3 and L6
    context['original_price_L1'] = str(original_price_L1)
    context['original_price_L3'] = str(original_price_L3)
    context['original_price_L6'] = str(original_price_L6)
    
    # calculate discounted prices 
    discounted_price_L1 = original_price_L1 * (1 - float(discount_rate))
    discounted_price_L3 = original_price_L3 * (1 - float(discount_rate))
    discounted_price_L6 = original_price_L6 * (1 - float(discount_rate))
       
    # discounted prices for L1, L3 and L6
    context['discounted_price_L1'] = str(discounted_price_L1)
    context['discounted_price_L3'] = str(discounted_price_L3)
    context['discounted_price_L6'] = str(discounted_price_L6)

    return render(request,'coupons/add_coupon_success.html',context)
    


def add_b2c_coupon_failure(request): 
    return HttpResponse("Your gift card code is not valid")  
    
    
    
# these functions are not used in the code base.
# I decided to implement coupon addition using an ajax component. 
# However, this would have required us to develop very large ajax response. 
# thus, we turned back to usual httpResponse approach, as all the page needed to be 
# updated.   
#def add_coupon_ajax_response(request): 
#
#    hashcode = request.POST['hashcode'] 
#    
#    user_profile = UserProfile.objects.get( user=request.user )
#            
#    try: 
      
      #todo: insecurity in puting the hashcode in query string
#      coupon = Coupon.objects.get(hashcode = hashcode)
#      coupon.user_profile = user_profile
#      coupon.save()          
           
      # get the updated list of gifts, and pricing.
        # adding a gift coupon might change the prices of all products. 
        # therefore, it is not efficient to handle coupon addition with a 
        # ajax feature, as all the pricing output might need to be updated. 
        
      
      #    
#      return render (request,'/coupons/ajax_response.html',context)
           
#      return HttpResponseRedirect("/coupons/add_coupon_success/"+hashcode+"/"+str(coupon.discount_rate)+"/")

#      except Coupon.DoesNotExist:
            
#            return HttpResponseRedirect("/coupons/add_coupon_failure/")
                

    
#    context = {}
#    context['added'] = True
#    context['hashcode'] = hashcode 
    
#    return render(request,'coupons/ajax_response.html',context)
    
    
#def add_coupon_ajax(request): 
    
#    context = {}    
#    context.update(csrf(request))
#    return render(request,'coupons/add_coupon_ajax.html',context)
    

