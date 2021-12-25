from django.urls import path
from . import views

urlpatterns = [
    path("", views.forum, name="WebPres Forum"),
    path("discussion/<int:myid>/", views.discussion, name="Discussions"),
    path("register/", views.UserRegister, name="Register"),
    path("login/", views.UserLogin, name="Login"),
    path("logout/", views.UserLogout, name="Logout"),
    path("myprofile/", views.myprofile, name="Myprofile"),
    path("plan/", views.plan, name="Plan for Donate or Sponsor"),
    path("terms/", views.terms, name="Terms & Conditions"),
    path("privacy/", views.privacy, name="Privacy Policy"),
]
