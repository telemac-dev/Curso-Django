from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse('<h1>Hello World</h1>')
