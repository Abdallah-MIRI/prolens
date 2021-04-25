from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from PIL import Image
from django.urls import reverse

# Create your models here.

# Creat Class Post
class Post(models.Model):
  pub_date = models.DateTimeField()
  title = models.CharField(max_length=100)
  img_alt = models.CharField(max_length=100)
  img_post = models.ImageField(default='default.jpg', upload_to='media')
  published = models.BooleanField(default=True)

  def __str__(self):
      return self.title

class About(models.Model):
  title = models.CharField(max_length=150)
  img_body = models.ImageField(default='default.jpg', upload_to='media')
  content_body = models.TextField()

  def __str__(self):
      return self.title
  


  