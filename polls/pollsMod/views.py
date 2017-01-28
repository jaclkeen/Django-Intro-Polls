# -*- coding: utf-8 -*
# ^^^^^^^^^^^^^^^^^^^^ - USED TO FIXED ERRORS GIVEN FOR COMMENTS

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Choice, Question
from django.core.urlresolvers import reverse
from django.utils import timezone

# This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.
def index(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }

    return render(request, 'pollsMod/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    model = { 'question': question }

    return render(request, 'pollsMod/detail.html', model)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    model = { 'question': question }

    return render(request, 'pollsMod/results.html', model)

def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        """ request.POST is a dictionary-like object that lets you access submitted data by key name. In this case,
        request.POST[choice] returns the ID of the selected choice, as a string. request.POST values are always strings.
        request.POST[choice] will raise KeyError if choice wasnt provided in POST data. The above code checks 
        for KeyError and redisplays the question form with an error message if choice isn’t given """
        selected_choice = q.choice_set.get(pk=request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(q.id,)))