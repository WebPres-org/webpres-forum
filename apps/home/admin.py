from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):

    # Text to put in each page's <h1> (and above login form).
    admin.site.site_header = 'WebPres.org'
    admin.site.site_title = 'services | ronyman.com'
    admin.site.index_title = 'ronyman.com | Web Development'



admin_site = MyAdminSite()