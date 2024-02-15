from slack.slack_init import slack_app,slack_handler

from .slack_init import lunch_poll, ADMINS


@slack_app.action("poll_vote")
def handle_poll_vote(ack, body, say):
    ack()
    if lunch_poll.is_poll_expired():
        say("Sorry, poll expired!!")
    else:
        slack_id = body.get('user').get("id")
        value = body.get("actions")[0].get("selected_option").get("value")
        ts = body.get("container").get("message_ts")
        
        if value == "True":
            print("ts--", lunch_poll.ts)  # Note: value of value is a string not Bool.
            result = lunch_poll.poll_yes(
                slack_id=slack_id,
                ts=ts
            )
        else:
            result = lunch_poll.poll_no(
                slack_id=slack_id,
                ts=ts
            )


@slack_app.message("##poll_count")
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