from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.template.context_processors import csrf

from .forms import MyUserCreationForm


def register_test(request):

    pass
#    if request.method == 'POST': #

#        form = MyUserCreationForm(request.POST)       
#        if form.is_valid():
##        
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password1']         
#            user = User.objects.create_user(username=username, password=password)   
#            return HttpResponse("Thanks for you registration.")
                    
#    else: 
#        form = MyUserCreationForm()

#    context = {}
#    context.update(csrf(request))
#    context['form'] = form
#    return render(request,'code_test/register_test.html',context)     
    

def contact_me_view(request):
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['pourranjbar.ar@gmail.com']
            if cc_myself:
                recipients.append(sender)
            # send_mail(subject, message, sender, recipients)
            return HttpResponse("Thanks for contacting us.")

        else:
            template = loader.get_template('code_test/contact_us.html')
            context = RequestContext(request, {'form': form})
            return HttpResponse(template.render(context))

    else:
        form = ContactForm()
        template = loader.get_template('code_test/contact_us.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))


def test_fun_1(request):

    if request.method == 'POST':
        # this means that we have been sent some data on the url

        # get the data out of the submitted data.
        form = KidForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']

            template = loader.get_template('code_test/process_data.html')
            context = RequestContext(request, {'name': name,
                                               'address': address})
            return HttpResponse(template.render(context))

        # redirect to the same page with the data populated in the form
        template = loader.get_template('code_test/kids_inquiery.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))

    else:
        # this means that this is the first time the form is reached.
        form = KidForm()
        template = loader.get_template('code_test/kids_inquiery.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))
