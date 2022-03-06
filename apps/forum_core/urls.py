from django.urls import path
from . import views
from django.shortcuts import render




urlpatterns = [
    path("", views.forum, name="Forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("myprofile/", views.myprofile, name="Myprofile"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("contact/", views.contact, name="contact"),
]
