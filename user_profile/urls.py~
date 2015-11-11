from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid),
    url(r'^register/$', views.register),
    url(r'^register_success/$', views.register_success),
    url(r'^password_change/$', auth_views.password_change,{'template_name':'user_profile/password_change.html'}),
	url(r'^password_change_done/$', auth_views.password_change_done,{'template_name':'user_profile/password_change_done.html'}),
    url(r'^myprofile/$', views.myprofile),
]
