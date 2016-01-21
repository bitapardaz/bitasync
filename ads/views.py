from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import KasperskyCounter

def kaspersky_android(request):

    # get counter from DB
    counter = KasperskyCounter.objects.all()[0]

    # increase it
    counter.clicks = counter.clicks + 1

    # save new value of the counter
    counter.save()

    return HttpResponseRedirect("http://irkaspersky.com/products/for-home/kaspersky-internet-security-for-android")
