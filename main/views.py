from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1>working!<h1>")
# Create your views here.


def v1(response):
    return HttpResponse("<h1>V1!<h1>")
