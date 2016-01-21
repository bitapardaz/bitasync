from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^kaspersky/$', views.kaspersky_android),
]
