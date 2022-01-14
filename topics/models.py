from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Keyword(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(max_length=255)
  followedbys = models.ManyToManyField(User)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('keyword-detail', kwargs={'pk': self.pk})