from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^test_view/$', views.test_fun_1),
    url(r'^contact_us/$', views.contact_me_view),
    url(r'^register_test/$', views.register_test),
    url(r'^test_progress_bar/$', views.test_progress_bar),
    url(r'^test_choicefield/',views.test_choicefield),
]
