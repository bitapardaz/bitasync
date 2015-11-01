from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_view/$', views.test_fun_1),
    url(r'^contact_me/$', views.contact_me_view),
]
