from django.db import models
from django.contrib.auth import get_user_model
from taggit.managers import TaggableManager


# Create your models here.

User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes')
