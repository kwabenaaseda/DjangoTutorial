from django.db import models
from typing import ClassVar

# Create your models here.

class Collection(models.Model):
    collection_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    collcover = models.CharField(max_length=1000)
    
    objects: ClassVar[models.Manager["Collection"]] 
    
    def __str__(self) -> str:
        return self.collection_name


class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    typ = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField()
    piececover = models.CharField(max_length=1000)
    
    objects: ClassVar[models.Manager["Piece"]] 
    
    def __str__(self) -> str:
        return self.title