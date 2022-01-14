from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from topics.models import Keyword
from ckeditor_uploader.fields import RichTextUploadingField


class Proposal(models.Model):
    title = models.CharField(max_length=100)
    business_model = models.TextField()
    hr_partner = models.TextField()
    finance = models.TextField()
    technology = models.TextField()
    partner_user_ecosystem = models.TextField()
    community = models.TextField()
    roadmap = models.TextField()
    competitor = models.TextField()
    marketcap = models.TextField()
    tokenomics = models.TextField()
    fomo = models.TextField() 
    content = RichTextUploadingField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    keywords = models.ManyToManyField(Keyword,max_length=255)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('proposal-detail', kwargs={'pk': self.pk})
