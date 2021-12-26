# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 ronyman.com
"""

from django.urls import path
from . import views

name = 'apps.user'


urlpatterns = [
    #path("", views.apps.index, name="index"),
    path("register", views.register_request, name="register")
]