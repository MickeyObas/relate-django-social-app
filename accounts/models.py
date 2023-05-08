from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(('First name'), max_length=35)
    last_name = models.CharField(('Last name'), max_length=35)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    profile_picture = models.ImageField(('Profile Picture'), upload_to='images/%Y/%m/%d')
    display_name = models.CharField(max_length=120, blank=True, null=True)
    birthdate = models.DateField()
    location = models
    
