from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, password, **extra_fields):
        """
        Creates and saves a new user.
        """
        if not password:
            raise ValueError("The password field must be set.")

        user = self.model(password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password, **extra_fields):
        """
        Creates and saves a new superuser.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(password, **extra_fields)
