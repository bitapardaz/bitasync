from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^traffic$', views.traffic),
    url(r'^statistics$', views.statistics),
    url(r'^subscribe$', views.subscribe),
    url(r'^unsubscribe$', views.unsubscribe),
    url(r'^services$', views.services),
    url(r'^history$', views.history),
    url(r'^events$', views.events),
    url(r'^incoming_message_notification$', views.incoming_message_notification),
    url(r'^incoming_message_delivery_notification$', views.incoming_message_delivery_notification),


]
