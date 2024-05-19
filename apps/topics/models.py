from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Topics(models.Model):
    name = models.CharField()
    topics = ArrayField(models.CharField(), blank=True)