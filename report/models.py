from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from topics.models import Keyword
from ckeditor_uploader.fields import RichTextUploadingField


class Record(models.Model):
    class Rate(models.TextChoices):
        Potential = 1, 'potential'
        Evaluating = 2, 'evaluating'
        NoPotential = 3, 'nopotential'
    niches = models.CharField(max_length=255)
    project = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    ecosystem = models.CharField(max_length=255)
    launch = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    website = models.URLField(max_length=255)
    twitter = models.CharField(max_length=255)
    overview = models.TextField(max_length=255)
    comment = models.TextField(max_length=255)
    rate = models.CharField(
        max_length = 2,
        choices=Rate.choices,
        default=Rate.Evaluating
    )
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword,max_length=255)


    def __str__(self):
        return self.project
        
    def get_absolute_url(self):
        return reverse('record-detail', kwargs={'pk': self.pk})
