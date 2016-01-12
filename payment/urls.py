from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<plan_name>\w\d)/$', views.pay_for_a_plan),
    url(r'^(?P<plan_name>\w\d)/(?P<token>[0-9A-Za-z]{1,20})/$', views.pay_for_a_plan_complete),
    url(r'^pay/$',views.pay),
    url(r'^gateway/$',views.gateway),
    url(r'^result/(?P<pending_purchase_id>[0-9A-Za-z]{1,32})/$',views.result),
]
