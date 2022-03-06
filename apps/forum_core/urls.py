
from django.urls import path, include
from . import views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from apps.forum_core import views as user_views




urlpatterns = [
    path("", views.forum, name="Forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('profile/', user_views.profile, name='profile'),
    #path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path("myprofile/", user_views.myprofile, name="Myprofile"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('tinymce/', include('tinymce.urls')),
    # For PasswordPresset

    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset',),
    path('admin/password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done',),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm',),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete',),
    path("myprofile/", views.myprofile, name="Myprofile"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("contact/", views.contact, name="contact"),
]
