from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



from django_countries.fields import CountryField

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(('First name'), max_length=35)
    last_name = models.CharField(('Last name'), max_length=35)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    profile_picture = models.ImageField(('Profile Picture'), upload_to='media/profile_images/%Y/%m/%d', default='profile-img.png')
    display_name = models.CharField(max_length=120, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    location = CountryField(blank_label="(Select Country)", null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name}'s Profile"
