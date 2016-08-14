from django.shortcuts import render

from django.http import HttpResponse

###########################################
### Integrated Panel ######################
###########################################
def traffic(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def statistics(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def subscribe(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def unsubscribe(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def services(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def history(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


def events(request):
    print request.GET.get('date')
    return HttpResponse("You are here.")


##########################################
#### Connectivity ########################
##########################################

def message_sending_request(sc,to,from_shortcode,service_id,charging_code,username,password,message,message_id):
    return True


def charge(sc,to,from_shortcode,service_id,charging_code,username,password,message,message_id):
    pass


def incoming_message_notification(request):
    return HttpResponse("Notification Received!",status=200)


def incoming_message_delivery_notification(request):
    return HttpResponse("Delivery Report Received!",status=200)
