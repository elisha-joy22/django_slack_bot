from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from datetime import datetime, timedelta
from abc import ABC
import qrcode
import jwt
import os
import base64

load_dotenv()

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
QR_CODE_LINK = os.environ.get("QR_CODE_LINK")



def generate_token(user_id,ts,secret_data):
    payload = {
        "user_id": user_id,
        "ts":ts,
        "secret_data": secret_data        
    }
    token = jwt.encode(payload,JWT_SECRET_KEY,algorithm='HS256')
    encoded_token = base64.urlsafe_b64encode(token.encode())
    decoded_token = encoded_token.decode()
    print(decoded_token)
    return decoded_token



def decode_token(encoded_token):
    # Decode the Base64 URL encoded token
    decoded_token = base64.urlsafe_b64decode(encoded_token)
    
    # Verify and decode the JWT token using the secret key
    try:
        payload = jwt.decode(decoded_token, JWT_SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Handle expired token
        return None
    except jwt.InvalidTokenError:
        # Handle invalid token
        return None


def generate_qr_code(link,channel_id):
    features = qrcode.QRCode(version=1,box_size=40,border=2)
    features.add_data(link)
    features.make(fit=True)

    generate_image = features.make_image(fill_color="black",back_color="white")
    #generate_image = qrcode.make("QR code for lunch")

    generate_image.save(f'{channel_id}.png')




