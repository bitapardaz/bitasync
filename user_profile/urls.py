from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^loggedin/$', views.loggedin),
    url(r'^invalid/$', views.invalid),
    url(r'^register/$', views.register),
    url(r'^register_success/$', views.register_success),
    url(r'^password_change/$', views.password_change),
    url(r'^myprofile/$', views.myprofile),

]



