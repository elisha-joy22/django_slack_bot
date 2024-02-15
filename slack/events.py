# slack_actions/events.py

from .slack_init import lunch_poll, ADMINS

def message_hello(message, say):
    print("inside message")
    user = message.get("user")
    print(f"user - {user}")
    print(f"admins {ADMINS}")
    if user in ADMINS:
        count = lunch_poll.get_poll_count()
        say(f"count: {count}")
    else:
        say(f"ayn nee ethaada ...!")
