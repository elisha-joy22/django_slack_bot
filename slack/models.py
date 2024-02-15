from django.db import models
from poll.models import Poll

class BotManager(models.Manager):
    def create_poll(self,poll_text,poll_start_datetime,poll_end_datetime,lunch_datetime):
        poll = Poll.objects.create(
            bot_id=self.bot_id,
            poll_text = poll_text,
            start_datetime=poll_start_datetime,
            end_datetime=poll_end_datetime,
            event_datetime=lunch_datetime,             
        )


    def get_last_poll(self):
        last_poll = Poll.objects.order_by('-event_datetime').first()
        return last_poll


# Create your models here.
class Bot(models.Model):
    bot_id = models.CharField(max_length=255)
    bot_name = models.CharField(max_length=255)

    objects = BotManager()