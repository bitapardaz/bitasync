"""bitasync URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bitasync_site import views

#from bitasync_site import views
#from user_profile import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bitasync/', include('bitasync_site.urls')),
    url(r'^accounts/', include('user_profile.urls')),
    url(r'^code_test/', include('code_test.urls')),  
    url(r'^guides/',include('guides.urls')), 
    url(r'^coupons/',include('coupons.urls')), 
#    url(r'^payment/',include('payment.urls')), 
]
