from django.contrib import admin


class AdminSite(admin.AdminSite):
    site_header = index_title = 'Administration'


admin_site = AdminSite(name="djangopoc")
