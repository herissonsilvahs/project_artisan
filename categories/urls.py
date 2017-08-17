from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^new/$', views.new, name='new'),
	url(r'^list/$', views.list_category, name='list'),
	url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
	#url(r'^status/(?P<pk>\d+)/active', views.activate, name='activate'),
	#url(r'^status/(?P<pk>\d+)/disable', views.deactivate, name='deactivate'),
	#url(r'^status/(?P<pk>\d+)/block', views.block, name='block')
]