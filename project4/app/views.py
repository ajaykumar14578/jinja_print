from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee>This is first view function</marquee>')

def propose(request):
    return HttpResponse('<h1>yes i love u</h1>')