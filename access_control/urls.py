from django.conf.urls import include, url
from django.contrib import admin
import views


urlpatterns = [
    url(r'^access/(?P<username>[a-zA-Z0-9_.-]+)/$',views.access),
]
