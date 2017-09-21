from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$', views.new, name='new'),
	#url(r'^list/$', views.list_category, name='list'),
	#url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
	#url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
]