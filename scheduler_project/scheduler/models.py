from django.db import models

# Create your models here.

class Schedule(models.Model):
    title = models.CharField(max_length=30)
    time = models.TimeField()
    date = models.DateField()
    place = models.CharField(max_length=20)
    memo = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

