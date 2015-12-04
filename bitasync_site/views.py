from django.http import HttpResponse, HttpResponseRedirect
from .models import Data_Transfer_Plan
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.core.mail import send_mail
from .forms import Contact_us

from models import Contact_Comment
from models import Purchase

from coupons.models import Coupon
from user_profile.models import UserProfile

from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from payment.utilities import Transaction

import hashlib

from utilities import utility_functions 

def thanks_contact_us(request):

    response = """
        <p> Thanks for contacting us.</p>
        <p> Click <a href="/"> here </a> to return home. </p> 
        
    """

    return HttpResponse(response)

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

        
            template = loader.get_template('bitasync_site/contact_us.html')
            context = RequestContext(request,args)
            return HttpResponse(template.render(context))
        
        
    else:
        form = Contact_us()
        
        args= {}
        args['form']=form

        
        template = loader.get_template('bitasync_site/contact_us.html')
        context = RequestContext(request,args)
        return HttpResponse(template.render(context))

def homepage(request):
      return render(request, 'bitasync_site/index.html')
      
      
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

    if request.method == "POST": 
        
        # check that the model chosen is correct. 
        
        valid_plans = ["L1","L3","L6","U1","U3","U6"]
        
        if plan_name not in valid_plans :
            raise Http404("Data transfer selected is not valid.")
         
        plan = Data_Transfer_Plan.objects.get(plan_name = plan_name) 
        
        # todo. when the transaction is being done, add the gateway. 
        transaction = Transaction(price=plan.price)    

        # payment_status = process_payment(request,plan_name)            
        payment_status = transaction.process_transaction()
        
        if payment_status == True:
         
            # send an email to the user. 
            subject = "Bit@Sync Activation"
            message = "Your software is activated."
            from_email = "outreach@bitasync.com" 
            recipient_list = [request.user.email]
            
            send_mail(subject=subject,
                     message=message,
                     from_email = from_email,
                     recipient_list=recipient_list, 
                     fail_silently=False)
            
            # add to the purchase table.
            new_purchase = Purchase()
            new_purchase.user = request.user
            new_purchase.data_transfer_plan = plan 
            new_purchase.gateway = "unspecified"
            new_purchase.save()

            hasher = hashlib.md5()   # save follow_up number using hash       
            hasher.update(str(new_purchase.id))
            follow_up_number = hasher.hexdigest()
            new_purchase.follow_up_number = follow_up_number
            new_purchase.save()
            
            
            # todo: create a statistics table and store the data for the managers. 
            # add to the statistics table.
            
            #return HttpResponseRedirect("/bitasync/activate/successful_payment/")
            #todo: put advertisement in this payment_success page. 
            return HttpResponseRedirect("/bitasync/activate/payment_success/" + plan.plan_name +"/" + follow_up_number + "/")
            
        else:
            # if the payment fails. 
            return HttpResponseRedirect("/bitasync/activate/payment_failed/"+ plan.plan_name +"/")
    else :
        # request.method is not POST  
        valid_plans = ["L1","L3","L6","U1","U3","U6"]
        
        if plan_name not in valid_plans :
            raise Http404("Data transfer selected is not valid.")
            
        else: 

            # todo: remove the database access. And instead, use a function from utilities.utility_functions to get the data about data_transfer_plans         
            plan = Data_Transfer_Plan.objects.get( plan_name = plan_name )
           
            # check if the user has any discount coupon.
            user_profile = UserProfile.objects.get( user = request.user )
            user_existing_coupons = Coupon.objects.filter( user_profile = user_profile )

#            original_prices = utility_functions.products_original_prices()
#            image_links = utility_functions.get_plan_image_link()
            
            # load data about the current plan selected.          
            selected_plan = utility_functions.create_temp_plan(plan, user_existing_coupons)
            
            # find data about the alternative plans
            # derive the set of 5 alternative plan                      
                         .             
            # set up the context 
            context={}
            context.update(csrf(request))
            context['selected_plan'] = selected_plan

            # setting the context, depending on whether the customer has any coupons available
            if not user_existing_coupons: 
                # if the customer does not have any coupon                           
                context['coupon_available'] = False
                
            else: 
                # if the customer has some coupons           
#                context['coupon_available'] = True
#                (coupon,discounted_prices) = product_discounted_prices(user_existing_coupons)
#                selected_plan.discounted_price = discounted_prices.get(selected_plan.plan_name)
                
                context['existing_coupons'] = user_existing_coupons 
            
            return render(request,'bitasync_site/payment_with_coupons.html',context)
            
            
@login_required       
def payment_failed(request,plan_name): 

    valid_plans = ["L1","L3","L6","U1","U3","U6"]
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
    
    

     


