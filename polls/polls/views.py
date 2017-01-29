from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

def index(request):
    return render(request, 'polls/register.html')

def login(request):
    return render(request, 'polls/login.html', { })
    
def logout(request):
    return HttpResponseRedirect(reverse('login'))

def createNewUser(request):
    return HttpResponseRedirect(reverse('polls:index'))