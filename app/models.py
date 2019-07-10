from django.db import models

# Create your models here.
class AgendaMaster(models.Model):
    title = models.TextField()
    description = models.TextField()