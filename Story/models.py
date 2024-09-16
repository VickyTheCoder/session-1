from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=150)
    story = models.CharField(max_length=6000)