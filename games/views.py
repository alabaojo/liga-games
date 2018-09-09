from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import request

from games.models import Team

def team(request, team_id):
    return HttpResponse("You're looking at team %s." % team_id)


def home(request):
    
    #return HttpResponse("You're looking at games.")
    return render(request, 'games/index.html')

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = 3344
       
    #num_authors = Author.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': "Game on!",
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)