from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hompage(request):
    return HttpResponse("my app")