from django.contrib.auth.views import logout
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'accounts:login'}, name='logout'),
   	url(r'^list/$', views.list_user, name='list'),
   	url(r'^detail/(?P<pk>\d+)$', views.detail, name="detail"),
	url(r'^status/(?P<pk>\d+)/active', views.activate, name='activate'),
	url(r'^status/(?P<pk>\d+)/disable', views.deactivate, name='deactivate'),
	url(r'^status/(?P<pk>\d+)/block', views.block, name='block'),
]
