from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request,"website/welcome.html",
                  {"meetings":Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at "+str(datetime.now()))

def about(request):
    return HttpResponse("I am a Computer Science student")