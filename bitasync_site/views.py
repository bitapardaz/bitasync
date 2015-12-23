from django.http import HttpResponse, HttpResponseRedirect
from .models import Data_Transfer_Plan
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.core.mail import send_mail
from .forms import Contact_us

from models import Contact_Comment


from coupons.models import Coupon
from user_profile.models import UserProfile

from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

import hashlib

from utilities import utility_functions

from coupons.forms import AddCouponForm

def thanks_contact_us(request):

    
    return render(request, 'bitasync_site/thanks_contact_us.html')
    

def contact_us(request): 
    
    
    
    if request.method == "POST":
    
        form = Contact_us(request.POST)
        
        if form.is_valid(): 
            
            # send an eamil to the user acknowledging that his message was received. 
            email = form.cleaned_data['email']
            email_message = """Thanks for contacting Bit@Sync.    
            Our customer service team will get in touch shortly.             
            """
            subject = "Thanks for Contacting Bit@Sync."
            from_email = "outreach@bitasync.com"
            recipient_list = [email]
            
            send_mail(subject=subject,
                     message=email_message,
                     from_email = from_email,
                     recipient_list=recipient_list, 
                     fail_silently=False)
                     
                     
            # add user message to the database. 
            
            comment = Contact_Comment()
            comment.name = form.cleaned_data['name']
            comment.message = form.cleaned_data['message']
            comment.email = email 
            comment.call_back_request = form.cleaned_data['call_back']
            comment.phone_number = form.cleaned_data['phone_number']
            
            comment.save()       
            
            return HttpResponseRedirect("/bitasync/thanks_contact_us/")
        
        else: 
            
            args= {}
            args.update(csrf(request))
            args['form']=form

        
            template = loader.get_template('bitasync_site/index.html')
            context = RequestContext(request,args)
            return HttpResponse(template.render(context))
        
        
    else:
        form = Contact_us()
        
        args= {}
        args['form']=form

        
        template = loader.get_template('bitasync_site/index.html')
        context = RequestContext(request,args)
        return HttpResponse(template.render(context))

def homepage(request):
      


	 return contact_us(request);


	#return render(request, 'bitasync_site/index.html')
      
      
def homepage2(request):
      return HttpResponse("Test Homepage. You are at www.bitasync.com")


def data_transfer_plans(request):

    # return thh list of data_transfer_plans as a list.
    plans = Data_Transfer_Plan.objects.all()

    if not plans:
        raise Http404("No data transfer plans found")

    template = loader.get_template('bitasync_site/data_transfer_plans.html')
    context = RequestContext(request, {'plan_list': plans})
    return HttpResponse(template.render(context))

@login_required
def activate_plan(request,plan_name): 

    # check that the model chosen is correct. 
    valid_plans = ["L1","L2","L5","U1","U3","U6"]
   
    user_profile = UserProfile.objects.get( user = request.user )
    
    context={}
    context.update(csrf(request))
    context['coupon_code_entered'] = False
    
        
    if plan_name not in valid_plans :
      raise Http404("Data transfer selected is not valid.")

    if request.method == "POST": 
        # a new coupon code has been entered. Check if the coupon is valid and enter the code.  
        
        context['coupon_code_entered'] = True     
        form = AddCouponForm(request.POST)
        
        if form.is_valid():
         
            hashcode = form.cleaned_data['hashcode']
           
            # associate the code to the customer profile 
            try: 
                coupon = Coupon.objects.get( hashcode = hashcode )
                coupon.user_profile = user_profile
                coupon.save()
                context['wrong_coupon_entered'] = False          

            except Coupon.DoesNotExist:
                # the coupon entered does not exist in the database
                context['wrong_coupon_entered'] = True
         
                
        else: 
            # form is not valid
            context['wrong_coupon_entered'] = True             
                
        
      
    
        # request.method is not POST  
        # do the pricing given the customer's coupons
        
    all_plans = Data_Transfer_Plan.objects.all()
    plan = utility_functions.get_plan_by_name(all_plans,plan_name)
           
        # check if the user has any discount coupon.
    user_existing_coupons = Coupon.objects.filter( user_profile = user_profile )

    selected_plan = utility_functions.create_temp_plan(plan, user_existing_coupons)
    alternative_plans = get_alternative_plans(all_plans,selected_plan, user_existing_coupons)
                                    
            # set up the context 

    context['selected_plan'] = selected_plan
    context['alt_plan_0'] = alternative_plans[0]
    context['alt_plan_1'] = alternative_plans[1]
    context['alt_plan_2'] = alternative_plans[2]
    context['alt_plan_3'] = alternative_plans[3]
    context['alt_plan_4'] = alternative_plans[4]
            
            # setting the context, depending on whether the customer has any coupons available
    if not user_existing_coupons: 
        context['coupon_available'] = False
                
    else: 
                # if the customer has some coupons           
        context['coupon_available'] = True
        context['existing_coupons'] = user_existing_coupons 
        
            
    add_coupon_form = AddCouponForm()
    context['add_coupon_form'] = add_coupon_form
            
    return render(request,'bitasync_site/payment_with_coupons.html',context)
            
            
@login_required       
def payment_failed(request,plan_name): 

    valid_plans = ["L1","L2","L5","U1","U3","U6"]
    if plan_name not in valid_plans :
        raise Http404("Data transfer selected is not valid.")
    else: 

        if request.method == "POST": 
            # we should never arrive here. 
            # this page contains Contact_us form.
            # when the form is submited, the request is posted to
            # /bitasync/thanks_contact_us, and not here!
            pass
            
        else: 
            context = {}

            form = Contact_us()
            context['plan_name'] = plan_name
            context['form'] = form
            
            return render(request,"bitasync_site/payment_failed.html",context)

@login_required
def payment_success(request,plan_name,follow_up_number): 
    
    context = {}
    context['plan_name'] = plan_name
    context['img'] = get_image_link(plan_name)
    context['follow_up_number'] = follow_up_number
    
    return render(request,'bitasync_site/payment_success.html',context)
    #todo: in this page, we can put advertisement related to the mobile phones.
    
    
def get_alternative_plans(all_plans, selected_plan, coupons): 
    alt_plans = [] 
    ordered_names = ["L1","L2","L5","U1","U3","U6"]
   
    for name in ordered_names: 
        if name != selected_plan.plan_name:
            alternative_plan = utility_functions.get_plan_by_name(all_plans, name)
            alternative_temp_plan = utility_functions.create_temp_plan(alternative_plan,coupons)
            alt_plans.append(alternative_temp_plan) 
    return alt_plans
       
    
    
def terms_conditions(request): 
    return render(request,'bitasync_site/terms_conditions.html')
    
def about_us(request): 
    return render(request,'bitasync_site/about_us.html')  
    
def test_function(request): 
    return HttpResponse("test")  
    
