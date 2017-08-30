from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^new/$', views.new, name='new'),
	url(r'^list/$', views.list_artifact, name='list'),
]