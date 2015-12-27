from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bulk_license_select_shop/$', views.bulk_license_select_shop),
]
