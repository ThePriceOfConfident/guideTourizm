from django.db import models
from django.contrib.auth.models import User
from Destination.models import Destination


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="User", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")
    profile_picture_url = models.ImageField(verbose_name="Profile Picture URL", upload_to="profile_pictures/", blank=True)
    bio = models.TextField(verbose_name="Biography", blank=True)
    phone = models.CharField(verbose_name="Phone", max_length=20, blank=True)
    email = models.EmailField(verbose_name="Email", blank=True)
    country = models.CharField(verbose_name="Country", max_length=100, blank=True)
    address = models.CharField(verbose_name="Address", max_length=200, blank=True)
    facebook = models.URLField(verbose_name="Facebook Profile", blank=True)
    favorite_destination = models.ForeignKey(Destination, verbose_name="Favorite Destination", related_name="favorited_by", blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return f"Profile of {self.user.username}"