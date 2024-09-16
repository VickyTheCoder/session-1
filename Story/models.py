from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharFiled(150)
    story = models.CharFiled(6000)