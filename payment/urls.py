from django.conf.urls import include, url

import views 

urlpatterns = [
    url(r'^test_payment/$', views.test_payment),
]
