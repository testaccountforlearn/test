from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>hello</h1>')

def new_func(request):
    pass