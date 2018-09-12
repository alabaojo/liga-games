from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import request

from games.models import Team, Match, Result, Season
import games.services_games as services_games

import requests
from games.services import service_front



def games(request):
    context = services_games.get_it()
    return render(request, 'games/games.html', context)


# First, define the Manager subclass.
 


def match(request, match_id):
    return HttpResponse("You're looking at match %s." % match_id)

def team(request, team_id):
    return HttpResponse("You're looking at team %s." % team_id)

def ratio(request, team_id):
    return HttpResponse("You're looking at team %s result win/loss ratioratio." % team_id)

def season(request, season_id):
    return HttpResponse("You're looking at matches of %s season." % season_id)


def season(request):
    season_info = {'teams':'y'}
    season_info= {'teams':[]}
    teams = []
    matches = []
    for member in Team.objects.all():
        teams.append(member)
    context=season_info['teams': teams, 'matches' : matches ]
    return render(request, 'games/index.html', context)

def index(request):
    teams = service_front.teams_info()
    matches = service_front.teams_info()
    context = {"brand": "Ford", "model": "Mustang", "year": 1964 }
    return render(request, 'games/index.html', context)