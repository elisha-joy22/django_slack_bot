from slack_sdk.errors import SlackApiError

class ContentPoster():
    def __init__(self,app):
        self.app = app 

    def post_content(self,channel_id,text,blocks=None):
        try:
            response = self.app.client.chat_postMessage(
                channel=channel_id,
                text=text,
                blocks=blocks
            )
            return response
        except SlackApiError as e:
            print(f"Error posting content: {e.response['error']}")


    def update_posted_content(self,channel_id,text,ts,blocks=None):
        print(f"channel in update_content\n{channel_id}\ntext{text}\nts{ts}")
        try:
            response = self.app.client.chat_update(
                channel=channel_id,
                ts=ts,
                text=text
                #blocks=blocks
            )
            return response
        except SlackApiError as e:
            print(f"Error posting content: {e.response['error']}")


    def post_file(self,channel_id,title):
        print("channel_id",channel_id)
        self.app.client.files_upload(
            file=f"{channel_id}.png",
            channels=channel_id,
            title=title
        )




class PollBlockBuilder():
    def __init__(self):
        pass
    
    def create_yes_no_poll_block(self, question, poll_expiry_datetime):
        poll_end_time = poll_expiry_datetime.strftime("%H:%M")
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{question}\n*(Please vote by selecting an option)*\nThis poll will expire at {poll_end_time}."
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "radio_buttons",
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Yes"
                                },
                                "value": "True"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "No"
                                },
                                "value": "False"
                            }
                        ],
                        "action_id": "poll_vote"
                    }
                ]
            }
        ]

        return blocks



