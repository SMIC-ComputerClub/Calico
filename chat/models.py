from django.db import models
from datetime import datetime
import pytz

def getTime():
    d = datetime.datetime.now()
    tz=pytz.timezone('Asia/Shanghai')
    time=tz.localize(d)
    return time.tzinfo
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now(pytz.timezone('Asia/Shanghai')), blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

