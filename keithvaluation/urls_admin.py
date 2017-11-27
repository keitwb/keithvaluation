from django.conf.urls import patterns, include, url

from .admin import kv_admin_site


urlpatterns = [
    url(r'', include(kv_admin_site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
]

