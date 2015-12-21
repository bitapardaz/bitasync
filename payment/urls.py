from django.conf.urls import include, url

from . import views 

urlpatterns = [
    url(r'^(?P<plan_name>\w\d)/$', views.pay_for_a_plan),
]
