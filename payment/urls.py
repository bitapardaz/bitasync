from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^(?P<plan_name>\w\d)/$', views.pay_for_a_plan),
    url(r'^initialise_payment/(?P<plan_name>\w\d)/$', views.initialise_payment_payline),
    url(r'^result_payline/(?P<pending_purchase_hashcode>[0-9A-Za-z]{1,32})/$',views.result_payline),
]
urlpatterns = format_suffix_patterns(urlpatterns)
