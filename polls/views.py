# from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("The ma):in page")

def info(request):
    return HttpResponse("This is second")


