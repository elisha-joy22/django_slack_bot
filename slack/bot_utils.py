from slack.slack_utils import ContentPoster
from datetime import datetime,timedelta
from dotenv import load_dotenv
import os

from poll_bot.utils import generate_qr_code,generate_token
from poll.models import Poll,PollUser
from slack.models import Bot


load_dotenv()

QR_CODE_LINK = os.environ.get("QR_CODE_LINK")



class LunchBot(ContentPoster):
    def __init__(self,app,bot_id,bot_name,channel_id):
        self.app= app
        self.bot_id= bot_id
        self.bot_name = bot_name
        self.channel_id = channel_id
        super().__init__(app)

    def create_lunch_poll(self,poll_start_datetime,poll_end_datetime,lunch_datetime):
        current_datetime = datetime.now().replace(microsecond=0)
        lunch_datetime = current_datetime.replace(hour=12,minute=30,second=0)+timedelta(days=1)
        question = f"Will you join us for lunch tomorrow {lunch_datetime}?"
        lunch_bot = Bot.objects.get_or_create(bot_id=self.bot_id,bot_name=self.bot_name)
        lunch_bot.objects.create_poll(
                                poll_text=question,
                                poll_start_datetime=poll_start_datetime,
                                poll_end_datetime=poll_end_datetime,
                                lunch_datetime=lunch_datetime
        )
        print("poll created!!")


    def post_poll_expired(self,poll):
        print("tssss",poll.ts)
        poll_count=poll.get_poll_count(poll.ts)
        poll.poll_closed = True
        poll.save()
        text1=f"No more responses, Poll expired for lunch {self.poll.event_datetime}. Thank you!!"
        text2 = f"\nTodays poll count - {poll_count}"
        text3 = f"\nThank you !!"
        text = text1 + text2 + text3
        self.update_posted_content(poll.channel_id,text=text,ts=poll.ts)
        print("post expired...")


    def get_last_poll(self):
        last_poll = Poll.objects.filter(bot_id=self.bot_id).order_by('-event_datetime').first()
        return last_poll


    def send_qr_code_to_users(self,poll):
        users = poll.get_polled_users(poll.ts)
        directory = "qr_code_images"
        os.makedirs(directory, exist_ok=True)
        for user_instance in users:
            user_slack_id = user_instance.slack_id
            poll_user_instance = PollUser.objects.get(user=user_instance,poll=poll)
            secret_data = poll_user_instance.poll_secret
            token = generate_token(user_slack_id,poll.ts,secret_data)
            link = QR_CODE_LINK + token
            generate_qr_code(link,user_slack_id)
            title="Hey, This is your QR code for verification for the lunch tomorrow\nEnjoy lunch!!"
            self.post_file(user_slack_id,title)
        try:
            #shutil.rmtree(directory)
            print(f"Directory {directory} and its contents removed successfully.")
        except Exception as e:
            print(f"An error occurred while removing directory: {e}")


