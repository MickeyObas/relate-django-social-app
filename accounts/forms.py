from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password2']


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture', 'display_name', 'birthdate', 'location']

