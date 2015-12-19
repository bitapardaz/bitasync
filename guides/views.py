from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def using_gbg(request): 
    return render(request,'guides/using_gbg.html')

    
