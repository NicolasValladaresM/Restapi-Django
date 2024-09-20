from django.db import models

# Create your models here.

class Programmer(models.Model):
    name = models.CharField(max_length=400)
    surname = models.CharField(max_length=400)
    nickname = models.CharField(max_length=400)
    age = models.PositiveSmallIntegerField()
    active= models.BooleanField(default=True)


class Animal(models.Model):
    name = models.CharField(max_length=400)
    age = models.PositiveSmallIntegerField()
    vertebled = models.BooleanField(default=True)
    quadriped= models.BooleanField(default=True)