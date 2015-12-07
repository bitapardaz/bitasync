from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^add_coupon/$', views.add_coupon_to_profile),
    url(r'^add_coupon_success/(?P<hashcode>(\d|\w)+)/(?P<discount_rate>(\d\.\d{2}))/$',views.add_coupon_success), 
    url(r'^add_b2c_coupon_failure/$',views.add_b2c_coupon_failure), 
]
