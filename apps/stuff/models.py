from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
      Firstname = models.CharField(max_length=255)
      Lastname = models.CharField(max_length=255)
      Email = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
      name = models.CharField(max_length=255)
      desc = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      UploadedBooks = models.ForeignKey(User, related_name = "UploadedBooks")
      likes = models.ManyToManyField(User, related_name="Likes")
