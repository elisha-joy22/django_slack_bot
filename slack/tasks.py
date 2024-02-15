from celery import shared_task
from django.utils import timezone
from dotenv import load_dotenv
from datetime import datetime,timedelta
from django.conf import settings
import os

from slack.bot_utils import LunchBot
from slack_init import slack_app
load_dotenv()

poll_start_time = settings.daily_poll_start_time
poll_end_time = settings.daily_poll_start_time
lunch_bot_id = settings.LUNCH_BOT_ID
lunch_bot_name = settings.LUNCH_BOT_NAME
lunch_channel_id = settings.LUNCH_BOT_CHANNEL_ID
lunch_time = settings.LUNCH_TIME


@shared_task
def post_lunch_poll():
    lunch_bot = LunchBot(slack_app,lunch_bot_id,lunch_bot_name,lunch_channel_id)
    current_datetime = datetime.now().replace(microsecond=0)
    poll_start_datetime = current_datetime + timedelta(hours=poll_start_time.hour, minutes=poll_start_time.minute),
    poll_end_datetime = current_datetime + timedelta(hours=poll_end_time.hour, minutes=poll_end_time.minute),
    lunch_datetime = current_datetime.replace(hour=lunch_time.hour,minute=lunch_time.minute)\
                        + timedelta(hours=lunch_time.hour, minutes=lunch_time.minute)\
                        +timedelta(days=1)
    lunch_bot.create_lunch_poll(
        poll_start_datetime=poll_start_datetime,
        poll_end_datetime=poll_end_datetime,
        lunch_datetime=lunch_datetime,        
    )
    lunch_bot.post_content(lunch_bot.channel_id)


@shared_task
def post_poll_expired():
    lunch_bot = LunchBot(slack_app,lunch_bot_id,lunch_bot_name,lunch_channel_id)
    poll = lunch_bot.get_last_poll()
    lunch_bot.post_poll_expired(poll)


@shared_task
def send_qr_code_to_users(ts):
    lunch_bot = LunchBot(slack_app,lunch_bot_id,lunch_bot_name,lunch_channel_id)
    poll = lunch_bot.get_last_poll()
    lunch_bot.send_qr_code_to_users(poll)