from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from djangopoc.djangopoc_main.admin import admin_site
from djangopoc.users.forms import UserChangeForm, UserCreationForm
from djangopoc.users.models import Organization, User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    class Meta:
        model = User


class OrganizationAdmin(admin.ModelAdmin):
    ...


admin_site.register(User, UserAdmin)
admin_site.register(Organization, OrganizationAdmin)
