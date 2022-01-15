# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.urls import path
from . import views
import apps.forum_core.views
from django.urls import path, reverse_lazy, include
from django.contrib.auth import views as auth_views

app_name = 'accounts'

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

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url=reverse_lazy('accounts:password_reset_done')
    ), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('password_reset_<uidb64>_<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('accounts:password_reset_complete')
    ), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),

    #path('tinymce/', include('tinymce.urls')),


]