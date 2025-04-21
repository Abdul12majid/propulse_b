from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from propulse_app.models import Hostel


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    profile_bio=models.TextField(null=True, blank=True, max_length=500)
    bookmarked = models.ManyToManyField(Hostel, related_name='saved_hostels', symmetrical=False, blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile=Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)