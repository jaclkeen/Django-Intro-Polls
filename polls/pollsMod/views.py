from django.shortcuts import render
from django.http import HttpResponse

# This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index'")

def detail(request, question_id):
    return HttpResponse("You're looking at question {0}".format(question_id))

def results(requst, question_id):
    response = "Your looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)