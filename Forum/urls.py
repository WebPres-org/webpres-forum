from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import apps.forum_core.views

urlpatterns = [
    # Forum_core
    path('admin/', admin.site.urls),
    path('', include('apps.forum_core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
