from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid),
    url(r'^register/$', views.register),
    url(r'^register_success/$', views.register_success),
    url(r'^password_change/$', views.my_password_change),
	url(r'^my_password_change_done/$', views.my_password_change_done),
	url(r'^password_reset/$',views.my_password_reset,name='password_reset'),
    url(r'^password_reset_done/$', views.my_password_reset_done),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.my_password_reset_confirm,name='password_reset_confirm'), 
    url(r'^password_reset_complete$',views.my_password_reset_complete,name='password_reset_complete'),  
    url(r'^myprofile/$', views.myprofile),
]

