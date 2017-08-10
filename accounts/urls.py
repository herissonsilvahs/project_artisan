from django.contrib.auth.views import login, logout
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'accounts:login'}, name='logout'),
   	url(r'^list/$', views.list_user, name='task'),
   	url(r'^detail/(?P<pk>\d+)$', views.detail, name="detail"),
	url(r'^status/(?P<pk>\d+)/active', views.activate, name='activate'),
	url(r'^status/(?P<pk>\d+)/disable', views.deactivate, name='deactivate'),
	url(r'^status/(?P<pk>\d+)/block', views.block, name='block'),
]
