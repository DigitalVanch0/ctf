from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name=''),
    path('challenges.html/', challenges, name='challenges'),
    path('scoreboard.html/', scoreboard, name='scoreboard'),
    path('teams.html/', teams, name='teams'),
    path('profile.html/', profile, name='profile')
]