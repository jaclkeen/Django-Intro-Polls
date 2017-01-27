from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

# This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }

    return render(request, 'pollsMod/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    model = { 'question': question }

    return render(request, 'pollsMod/detail.html', model)

def results(requst, question_id):
    response = "Your looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)