from django.http import HttpResponse, HttpResponseRedirect
from .models import Data_Transfer_Plan
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from django.core.mail import send_mail
from .forms import Contact_us

from models import Contact_Comment
from django.template.context_processors import csrf

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from payment.utilities import Transaction

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
            
            
            # add to the statistics table.
            
            #return HttpResponseRedirect("/bitasync/activate/successful_payment/")
            return HttpResponse("""Thanks for your order. 
                                   Your account is now activated.
                                   A confirmation email has been sent to your email.""")
            
        else: 
        
            return HttpResponseRedirect("/bitasync/activate/" + plan_name + "/")
            
            
    else : 
    
        valid_plans = ["L1","L3","L6","U1","U3","U6"]
        
        if plan_name not in valid_plans :
            raise Http404("Data transfer selected is not valid.")
            
        else: 
        
            plan = Data_Transfer_Plan.objects.get(plan_name = plan_name)
            context={}
            context['plan'] = plan
            
            if plan_name == "L1":
                image_link = ""
            elif plan_name == "L3": 
                image_link = ""
            elif plan_name == "L6": 
                image_link = "" 
            elif plan_name == "U1": 
                image_link = "" 
            elif plan_name == "U3": 
                image_link = ""
            elif plan_name == "U6": 
                image_link = ""
                
            context['image_link'] = image_link
            
            context.update(csrf(request))
            
            return render(request,'bitasync_site/payment.html',context)

