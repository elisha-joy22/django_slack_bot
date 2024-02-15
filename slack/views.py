from slack_bolt import App
from slack_bolt.adapter.django import SlackRequestHandler
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import os
from django.conf import settings
from slack.slack_init import slack_handler



# Create your views here.
class VerifyPollTokenView(APIView):
    def get(self,request):
        poll_token = request.GET.get("poll_token")
        return render(request,"submit_secret_key.html",poll_token=poll_token)

    def post(self,request):
        secret_key = request.POST.get("secret_key")
            
        if secret_key!=settings.JWT_SECRET_KEY:
            print("failed")
            return render("not_verified.html")
                    

class SlackEventsViewSet(APIView):
    def post(self, request):
        print("event recorded")
        if request.headers.get("Content-Type") == "application/json":
            data = request.data
            if "challenge" in data:
                return Response(data={"challenge": data["challenge"]}, status=status.HTTP_200_OK)
            return slack_handler.handle(request)
        else:
            return Response(status=status.HTTP_200_OK, data={})



class SlackPollViewSet(APIView):
    def post(self, request):
        return slack_handler.handle(request)



