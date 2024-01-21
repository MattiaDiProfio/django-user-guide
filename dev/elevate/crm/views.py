from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def register(request):
    return HttpResponse("Registration page")
