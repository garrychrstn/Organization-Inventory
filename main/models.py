from django.db import models
from . choices import *


# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=60)
    penerima = models.CharField(max_length=30, default='belum diisi')
    type = models.CharField(max_length=20)
    amount = models.IntegerField()
    owner = models.CharField(max_length=20)
    dateIn = models.DateField()
    desc = models.CharField(max_length=100)
    location = models.CharField(max_length=20, default='lemari abu')
    
class Events(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateField()
    desc = models.CharField(max_length=100)
    img = models.CharField(max_length=100, default='no img')
    reg = models.CharField(max_length=100)
    upt = models.DateTimeField(auto_now_add=True, null=True)

class Members(models.Model):
    nim = models.IntegerField(default=0)
    name = models.CharField(max_length=40)
    position = models.CharField(
        max_length=30,
        choices=POSITION_OPTION,
    )
    year = models.IntegerField()
    program = models.CharField(max_length=30)
    potrait = models.CharField(max_length=100, default='NO PHOTO')


class Articles(models.Model):
    pass

class Cash(models.Model):
    name = models.ForeignKey(Members, on_delete=models.CASCADE)
    jan = models.BooleanField(default=False)
    feb = models.BooleanField(default=False)
    mar = models.BooleanField(default=False)
    apr = models.BooleanField(default=False)
    may = models.BooleanField(default=False)
    jun = models.BooleanField(default=False)
    jul = models.BooleanField(default=False)
    aug = models.BooleanField(default=False)
    sep = models.BooleanField(default=False)
    
