from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.forum_core import views as user_views
from django.shortcuts import render

#from .forms import UserRegisterForm, UserUpdateForm, EditProfileForm, ProfileForm
#from .models import Profile, UpdateProfileForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.http import HttpResponse

urlpatterns = [
    # Forum_core
    path('admin/', admin.site.urls),
    path('', include('apps.forum_core.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
