from django.conf.urls import url

from . import views

urlpatterns = [
    url('^data_transfer_plans$', views.data_transfer_plans, name='data_transfer_plans'),
]
