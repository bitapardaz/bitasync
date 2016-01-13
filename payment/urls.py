from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<plan_name>\w\d)/$', views.pay_for_a_plan),
    url(r'^initialise_payment/(?P<plan_name>\w\d)/$', views.initialise_payment_payline),
    url(r'^(?P<plan_name>\w\d)/(?P<token>[0-9A-Za-z]{1,20})/$', views.pay_for_a_plan_complete),
    url(r'^result_payline/(?P<pending_purchase_hashcode>[0-9A-Za-z]{1,32})/$',views.result_payline),


]
