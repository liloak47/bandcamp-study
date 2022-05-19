from django.db import models
from musicians.models import Musician
# Create your models here.

class Tags(models.Model):
    name = models.CharField(max_length=255)

class Album(models.Model):
    title = models.CharField(max_length=255)
    
    musicians  = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

