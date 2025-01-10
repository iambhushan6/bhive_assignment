from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, username, phone,  password=None):
        if username is None:
            raise TypeError("User should have an username!")
        if phone is None:
            raise TypeError("User should have an mobile no!")

        user = self.model( username=username, phone=phone )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, phone, password=None):
        if password is None:
            raise TypeError("Password should not be None!")
        user = self.create_user( username, phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, db_index=True)
    phone = models.CharField(max_length=12, unique=True, db_index=True)
    is_seller = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = [ 'username' ]

    objects = UserManager()

    def __str__(self):
        return self.phone

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }