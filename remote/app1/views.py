from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return HttpResponse("<div> <ul><li>Home</li><li>Preview</li></ul><h1>Hello, My name is Rocky</h1> </div>")


def preview1(request):
    return HttpResponse("<div> <h1>C'est la vie</h1> </div>")


def preview2(request):
    return HttpResponse("<div> <h1>Jonas Brothers</h1> </div>")


def preview3(request):
    return HttpResponse("<div>  <h1>Get you're vaccines right away!</h1> </div>")


def preview4(request):
    return HttpResponse("<div>  <h1>World War|||</h1> </div>")



