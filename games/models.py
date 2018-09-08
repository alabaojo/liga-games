from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    player = models.ForeignKey(Player)

class Team(models.Model):
    name = models.CharField(max_length=60))
    location = models.CharField(max_length=60))
    stadium = models.CharField(max_length=200)
    

class Player(models.Model):
    name = models.CharField(max_length=60))
    club_id = models.ForeignKey(Club)

    class Meta:
        ordering = ('club_id',)
    
class Goal(models.Model):
    score_time = models.FloatField(max_length=6))
    scorer_id = models.ForeignKey(Player)
    is_own_goal = models.BooleanField(default=false)

class Match(models.Model):
    home_team = models.ForeignKey(Team)
    away_team = models.ForeignKey(Team)
    match_date =  models.DateTimeField(default=datetime.now())
    home_team_goals = models.IntegerField(default=0)  
    away_team_goals = models.IntegerField(default=0)    