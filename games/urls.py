from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('/', views.index, name='index'),
    # ex: /polls/5/
    path('<int:team_id>/', views.team, name='team'),
    # ex: /games/5/ratio/
    path('<int:team_id>/ratio/', views.ratio, name='ratio'),
      
    #path('<int:seasion_id>/<int:match_id>', views.match, name='match'),
        # ex: /games  current season games
    path('season/', views.games, name='season'),
    path('', views.index, name='index'),

    
   
]