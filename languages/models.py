from django.db import models
from django.utils import timezone

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    developer_company = models.CharField(max_length=255, blank=False, null=True)
    predescessors = models.CharField(max_length=255, blank=False, null=True)
    added = models.DateTimeField(default=timezone.now)


class Programmer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    languages = models.ManyToManyField(Language)

    created_at models.DateTimeField(auto_now_add= True)
    modified_at = models.DateTimeField(auto_now=True)