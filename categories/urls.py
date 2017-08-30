from django.conf.urls import url
from . import views

urlpatterns = [
	#url(r'^new/$', views.new, name='new'),
	url(r'^list/$', views.list_category, name='list'),
	url(r'^detail/(?P<pk>\d+)$', views.detail, name='detail'),
	url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
	url(r'^subcategories/list/$', views.list_subcategory, name='list_subcategory'),
	url(r'^subcategories/detail/(?P<pk>\d+)$', views.detail_subcategory, name='detail_subcategory'),
	url(r'^subcategories/delete/(?P<pk>\d+)$', views.delete_subcategory, name='delete_subcategory'),
    url(r'^subcategories/materials/list/$', views.list_material, name='list_material'),
    url(r'^subcategories/materials/detail/(?P<pk>\d+)$', views.detail_material, name='detail_material'),
    url(r'^materials/detail/(?P<pk>\d+)$', views.delete_material, name='delete_material'),
]