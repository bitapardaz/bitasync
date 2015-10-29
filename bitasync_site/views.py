from django.shortcuts import render
from django.http import HttpResponse
from .models import Data_Transfer_Plans

def homepage(request):
    return HttpResponse("This is the homepage")

def data_transfer_plans(request):
    # return teh list of data_transfer_plans as a list.

    plans = Data_Transfer_Plans.objects.all()
    
    return HttpResponse("the list of data transfer plan")
