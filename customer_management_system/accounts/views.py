from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello buddy it's Home page")

def customer(request):
    return HttpResponse("Hello buddy it's Customer page")

def product(request):
    return HttpResponse("Hello buddy it's Product page")