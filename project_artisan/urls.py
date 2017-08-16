from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^artisans/', include('artisans.urls', namespace='artisans')),
    url(r'^addresses/', include('addresses.urls', namespace='addresses')),
    url(r'^admin/', admin.site.urls),
]
