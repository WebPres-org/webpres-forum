from django.contrib import admin
# Register your models here.
from .models import Post, Replie, Profile



admin.site.register(Post)
admin.site.register(Replie)
admin.site.register(Profile)

#### Add custom admin templates
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres'
    admin.site.site_title = 'WebPres Forum Admin'
    admin.site.index_title = 'Forum Admin'


admin_site = MyAdminSite()

