from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/(?P<pk>\d+)$', views.new_artifact, name='new'),
    url(r'^list/$', views.list_artifact, name='list'),
    url(r'^detail/(?P<pk>\d+)$', views.detail_artifact, name='detail'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_artifact, name='delete'),
]
