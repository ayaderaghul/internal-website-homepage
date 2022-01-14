from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from topics.models import Keyword
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword,max_length=255)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
