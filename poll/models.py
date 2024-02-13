from django.db import models
from user.models import User
import datetime

# Create your models here.
class PollManager(models.Manager):
    def active_polls(self):
        return self.filter(end_date_time__gte=datetime.now())

    def is_poll_expired(self,ts):
        poll = self.get(ts=ts)
        return poll.end_date_time <= datetime.now()


class Poll(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateField()
    event_date_time = models.DateField()
    poll_text = models.CharField(max_length=255)
    ts = models.CharField(max_length=255)
    count = models.IntegerField()
    users = models.ManyToManyField(User,related_name='polls')

    objects = PollManager()

    def __str__(self):
        return self.poll_text
    
