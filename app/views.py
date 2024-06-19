from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def likki(request):
    return HttpResponse('<h1><marquee>likkii where are you going...........</marquee></h1>')
def jay(request):
    return HttpResponse('<h1><marquee>hey jay how are you?...........</marquee></h1>')