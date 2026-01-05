from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Hi Welcome to shop home page")

def product(request):
    return HttpResponse("This is Product Page")