from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




import apps.home.views
import apps.user.views

urlpatterns = [
    #Home App
    path('admin/', admin.site.urls),
    path("", apps.user.views.forum, name="forum"),
    path("privacy/", apps.home.views.privacy, name="privacy"),
    path("terms/", apps.home.views.terms, name="terms"),
    path("contact/", apps.home.views.contact, name="contact"),
    path('tinymce/', include('tinymce.urls')),
    path("services/", apps.home.views.services, name="services"),
    #path("register/", apps.home.views.register, name="register"),
    #path("login/", apps.home.views.login, name="login"),
    # User App
    path('', include('apps.user.urls')),
    path("register/", apps.user.views.register_request, name="register"),
    path("login/", apps.user.views.login_request, name="login"),
    path("myprofile/", apps.user.views.profile, name="myprofile"),
    path("logout/", apps.user.views.logout_request, name= "logout"),
    path("password_reset/", apps.user.views.password_reset, name= "password_reset"),

    #path("register/", apps.user.views.register, name="register"),
    #path("login/", apps.user.views.login, name="login"),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
