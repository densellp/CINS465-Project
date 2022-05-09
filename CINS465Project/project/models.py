from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class testTable(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                        primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    likes = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.profile.user.username