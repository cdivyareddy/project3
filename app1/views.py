from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def redme(request):
    return HttpResponse('i am using redme mobile..........')
