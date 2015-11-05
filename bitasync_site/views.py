from django.http import HttpResponse
from .models import Data_Transfer_Plan
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render


def homepage(request):
      return render(request, 'bitasync_site/index.html')


def data_transfer_plans(request):
    # return teh list of data_transfer_plans as a list.
    plans = Data_Transfer_Plan.objects.all()

    if not plans:
        raise Http404("No data transfer plans found")

    template = loader.get_template('bitasync_site/data_transfer_plans.html')
    context = RequestContext(request, {'plan_list': plans})
    return HttpResponse(template.render(context))
