from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return HttpResponse("<div> <h1> We made it out the hood</h1> </div>")


def preview1(request):
    return HttpResponse("<div> <h1>God Bless Nigeria</h1> </div>")


def preview2(request):
    return HttpResponse("<div> <h1>Ignorance s bliss</h1> </div>")


def preview3(request):
    return HttpResponse("<div>  <h1>100</h1> </div>")


def preview4(request):
    return HttpResponse("<div>  <h1>100</h1> </div>")



