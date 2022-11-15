from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings

from .admin import kv_admin_site

urlpatterns = static('content/media/', document_root=settings.MEDIA_ROOT) \
  + static('content/static/', document_root=settings.STATIC_ROOT) \
  + [
      path(r'', kv_admin_site.urls),
      re_path(r'^grappelli/', include('grappelli.urls')),
  ]

