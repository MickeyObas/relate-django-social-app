from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import CustomUser, Profile

@receiver(post_save, sender=CustomUser)
def build_profile(sender, instance, created, **kwargs):
    if created:
        user_object = instance
        Profile.objects.create()

