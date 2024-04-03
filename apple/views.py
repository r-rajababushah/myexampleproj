from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def mypage(request):
    return render(request, "mypage.html", {'val': 'rajababushah page'})