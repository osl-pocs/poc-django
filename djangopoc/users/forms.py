from django.contrib.auth.forms import UserCreationForm

from djangopoc.users.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'


class UserChangeForm(UserCreationForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    class Meta:
        model = User
        fields = '__all__'
