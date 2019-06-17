from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    developer_company = models.CharField(max_length=255, blank=True, null=True)
    precessors = models.CharField(max_length=255, blank=True, null=True)