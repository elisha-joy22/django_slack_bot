from django.urls import path
from slack.views import VerifyPollTokenView,SlackPollViewSet,SlackEventsViewSet


urlpatterns = [
    path('poll',SlackPollViewSet.as_view(),name="slack-poll"),
    path('poll/verify',VerifyPollTokenView.as_view(),name="slack-poll-verify"),
    path('events',SlackPollViewSet.as_view(),name='slack-events')
]
