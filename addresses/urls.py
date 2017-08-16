from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/artisan/(?P<pk>\d+)', views.create, name='create'),
]