from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    msg = "hey"
    return HttpResponse(msg)