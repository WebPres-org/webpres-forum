from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




import apps.home.views
import apps.user.views

urlpatterns = [
    #Home App
    path('admin/', admin.site.urls),
    path("privacy/", apps.home.views.privacy, name="privacy"),
    path("terms/", apps.home.views.terms, name="terms"),
    path("contact/", apps.home.views.contact, name="contact"),
    path('tinymce/', include('tinymce.urls')),
    path("services/", apps.home.views.services, name="services"),

    # User App
    path("", apps.user.views.forum, name="forum"),
    path('', include('apps.user.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
