from django.db import models

# Create your models here.
class board(models.Model):
    bname = models.CharField(max_length=20)
    bemail = models.CharField(max_length=500)
    bsite = models.CharField(max_length=500)
    bleave = models.TextField()