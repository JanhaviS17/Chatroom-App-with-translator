from django.db import models
from datetime import datetime

class Room_Details(models.Model):
    Room_Name = models.CharField(max_length=1000)
    Password = models.CharField(max_length=100)
    Created_By = models.CharField(max_length=100)
    Created_dttm = models.DateTimeField(default=datetime.now, blank=True)


class Message_Details(models.Model):
    Message = models.CharField(max_length=1000000000)
    Delivered_dttm = models.DateTimeField(default=datetime.now, blank=True)
    User = models.CharField(max_length=100)
    room_name=models.CharField(default="NULL",max_length=1000)

# Create your models here.
