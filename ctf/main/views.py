from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


menu = [{'title': "scoreboard", 'url_name': "scoreboard"},
        {'title': "teams", 'url_name': "teams"},
        {'title': "challenges", 'url_name': "challenges"},
        {'title': "main", 'url_name': "''"}]

def index(request):
    return render(request, 'main/index.html')


def challenges(request):
    #result = Task.objects.task()
    count = Task.objects.all().count
    form = TaskForm()
    return render(request, 'main/challenges.html') #{'form': form}, {'result': result}, 'count': count)

def scoreboard(request):
    return render(request, 'main/scoreboard.html')

def teams(request):
    return render(request, 'main/teams.html')

def profile(request):
    return render(request, 'main/profile.html')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'localhost/register.html'
    success_url = reverse_lazy('login')


 def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
