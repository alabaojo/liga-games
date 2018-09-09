from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.home, name='home'),
    # ex: /polls/5/
    #path('<int:team_id>/', views.team, name='team'),
    # ex: /polls/5/location/
    #path('<int:team_id>/stadium/', views.stadium, name='stadium'),

]