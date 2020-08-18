from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        from djangopoc.users.models import Organization

        organization = Organization.objects.get(pk=1)
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            organization=organization,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
