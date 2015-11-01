from django.http import HttpResponse
from django.template import RequestContext, loader
from .forms.forms import KidForm


def contact_me_view(request):
    

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

    else:
        # this means that this is the first time the form is reached.
        form = KidForm()
        template = loader.get_template('code_test/kids_inquiery.html')
        context = RequestContext(request, {'form': form})
        return HttpResponse(template.render(context))
