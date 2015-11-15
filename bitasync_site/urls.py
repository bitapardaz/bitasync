from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^data_transfer_plans$', views.data_transfer_plans,
        name='data_transfer_plans'),
    url(r'/contact_us/$',views.contact_us),
    url(r'/thanks_contact_us/$',views.thanks_contact_us),
]
