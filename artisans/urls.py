from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.new, name='new'),
    url(r'^list/$', views.list_artisan, name='list'),
    url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
    url(r'^status/(?P<pk>\d+)/active', views.activate, name='activate'),
    url(r'^status/(?P<pk>\d+)/disable', views.deactivate, name='deactivate'),
    url(r'^artesaos/$', views.list_artisans_users, name='list_artisan_users'),
    url(r'^artesao/(?P<pk>\d+)$', views.show_artisan_user, name='show_artisan_user'),
]
