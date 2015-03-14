from django.conf.urls import patterns, include, url

from .admin import kv_admin_site


urlpatterns = patterns('',
    url(r'', include(kv_admin_site.urls)),
)

