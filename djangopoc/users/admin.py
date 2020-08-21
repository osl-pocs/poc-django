from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from djangopoc.djangopoc_main.admin import admin_site
from djangopoc.users.forms import UserChangeForm, UserCreationForm
from djangopoc.users.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    class Meta:
        model = User


admin_site.register(User, UserAdmin)
