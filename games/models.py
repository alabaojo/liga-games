from django.db import models
from django.utils import timezone

from games.constants import DEFAULT_LEAGUE


class Result(models.Model):
    result_order = models.IntegerField()
    point_team1 = models.IntegerField()
    point_team2 = models.IntegerField()


class Team(models.Model):
    team_order = models.IntegerField()
    name = models.CharField(max_length=40, unique=True)
    alias = models.CharField(max_length=20)


class Match(models.Model):
    match_order = models.IntegerField()
    team_id = models.ManyToManyField(Team)
    is_home_match = models.BooleanField(default=False)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Season(models.Model):
    season_code = models.DateTimeField(blank=True)
    matches = models.ManyToManyField(Match)


class League(models.Model):
    league_code = models.CharField( max_length=3)
    match_id = models.ManyToManyField(Match)




