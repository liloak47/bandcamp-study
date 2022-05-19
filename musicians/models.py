from statistics import mode
from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    instrument = models.CharField(max_length=255)


class Bio(models.Model):
    musician = models.OneToOneField(Musician, on_delete=models.CASCADE)
    hometown = models.CharField(max_length=255)