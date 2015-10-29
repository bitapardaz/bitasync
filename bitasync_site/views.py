from django.http import HttpResponse
from .models import Data_Transfer_Plan
from django.template import RequestContext, loader
from django.http import Http404


def homepage(request):
    return HttpResponse("This is the homepage")


def data_transfer_plans(request):
    # return teh list of data_transfer_plans as a list.
    plans = Data_Transfer_Plan.objects.all()

    if not plans:
        raise Http404("No data transfer plans found")

    template = loader.get_template('bitasync_site/data_transfer_plans.html')
    context = RequestContext(request, {'plan_list': plans})
    return HttpResponse(template.render(context))
