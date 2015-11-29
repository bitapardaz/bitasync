from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^add_coupon/$', views.add_coupon_to_profile),
    url(r'^add_b2c_coupon_success/(?P<hascode>(\d|\w)+)\$',views.add_b2c_coupon_success)      
]
