from django.shortcuts import render
from django.http import HttpResponse

# This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index'")
