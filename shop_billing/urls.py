from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bulk_license_input_shop/$', views.bulk_license_input_shop_username),
    url(r'^bulk_license_create/(?P<fusername>.+)/$', views.bulk_license_create),
    url(r'^bulk_license_create_done/(?P<shop_username>.+)/(?P<plan_name>\w\d)/(?P<copies>(\d)+)/$', views.bulk_created_done),
]
