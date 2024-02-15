from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime,time
from celery.schedules import crontab
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = 'django-insecure-8yula%q3hm74+e4&9+^lp23f(5%^5sng+#v%)hmfe1yw^y08q+'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'poll_bot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'poll_bot.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SLACK_LUNCH_TOKEN = os.environ.get("SLACK_LUNCH_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.environ.get("SLACK_SIGNING_SECRET")
LUNCH_CHANNEL_ID = os.environ.get("LUNCH_CHANNEL_ID")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
ADMINS = os.environ.get("ADMINS")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
QR_CODE_LINK = os.environ.get("QR_CODE_LINK")
LUNCH_BOT_ID = os.environ.get("LUNCH_BOT_ID")
LUNCH_BOT_NAME = os.environ.get("LUNCH_BOT_NAME")

daily_poll_start_time = time(hour=6,minute=7)
daily_poll_end_time =  time(hour=6,minute=11)
lunch_time = time(hour=12,minute=30)




# settings.py

CELERY_BEAT_SCHEDULE = {
    'post-lunch-poll': {
        'task': 'your_app.tasks.post_lunch_poll',
        'schedule': crontab(hour=daily_poll_start_time.hour, minute=daily_poll_start_time.minute),
    },
    'post-poll-expired': {
        'task': 'your_app.tasks.post_poll_expired',
        'schedule': crontab(hour=daily_poll_end_time.hour, minute=daily_poll_end_time.minute),
    },
    'send-qr-code-to-users': {
        'task': 'your_app.tasks.send_qr_code_to_users',
        'schedule': crontab(hour=daily_poll_end_time.hour, minute=daily_poll_end_time.minute + 1),
    },
}
