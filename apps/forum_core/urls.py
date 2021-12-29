# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
import apps.forum_core.views


urlpatterns = [
    path("forum", views.forum, name="forum"),
    path("", apps.forum_core.views.forum, name="forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    path("register/", views.UserRegister, name="Register"),
    #path("login/", views.UserLogin, name="Login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path("logout/", views.UserLogout, name="Logout"),
    path("myprofile/", apps.forum_core.views.myprofile, name="Myprofile"),
    path("privacy/", apps.forum_core.views.privacy, name="privacy"),
    path("terms/", apps.forum_core.views.terms, name="terms"),
    path("contact/", apps.forum_core.views.contact, name="contact"),
    #path('tinymce/', include('tinymce.urls')),


]