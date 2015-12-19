from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^using_gbg/$',views.using_gbg)
]
