from django.urls import path, re_path, include

from .admin import kv_admin_site


urlpatterns = [
    path(r'', kv_admin_site.urls),
    re_path(r'^grappelli/', include('grappelli.urls')),
]

