# slack_integration/slack_init.py

from slack_bolt import App
from slack_bolt.adapter.django import SlackRequestHandler
from django.conf import settings

# Initialize the Slack Bolt app



slack_app = App(
    token=settings.SLACK_LUNCH_TOKEN,
    signing_secret=settings.SLACK_SIGNING_SECRET
)

# Create the Slack request handler
slack_handler = SlackRequestHandler(slack_app)
