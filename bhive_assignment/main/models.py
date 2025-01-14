from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.



AMC_CODES = {
    "BirlaSunLifeMutualFund_MF",
    "DSP_MF",
    "SBIMutualFund_MF",
    "TATAMutualFund_MF",
    "FRANKLINTEMPLETON",
    "PPFAS_MF",
    "HSBCMUTUALFUND_MF"
}

class UserManager(BaseUserManager):

    def create_user(self, username, email,  password=None):
        if username is None:
            raise TypeError("User should have an username!")
        if email is None:
            raise TypeError("User should have an email ID!")

        user = self.model( username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Password should not be None!")
        user = self.create_user( username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, db_index=True)
    email = models.CharField(max_length=30, unique=True, db_index=True)
    is_seller = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username' ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
    

class FundHouse(models.Model):

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    

class Portfolio(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    scheme_name = models.CharField(max_length=100)
    scheme_code = models.CharField(max_length=20)
    scheme_meta_data = models.JSONField(null=True, blank=True, default={})
    amount = models.PositiveIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'scheme_name', 'scheme_code'], name='unique_user_and_scheme')
        ]

