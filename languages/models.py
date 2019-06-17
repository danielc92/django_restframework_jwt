from django.db import models
from django.utils import timezone

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    developer_company = models.CharField(max_length=255, blank=True, null=True)
    predescessors = models.CharField(max_length=255, blank=True, null=True)
    added = models.DateTimeField(default=timezone.now)
