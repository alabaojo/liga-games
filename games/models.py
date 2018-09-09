from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    stadium = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Player(models.Model):
    name = models.CharField(max_length=60)
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)

    class Meta:
        ordering = ('team_id',)

    def __str__(self):
        return self.name 
    
class Goal(models.Model):
    score_time = models.FloatField(max_length=6)
    scorer_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    is_own_goal = models.BooleanField(default=False)

class Match(models.Model):
    teams_id = models.ManyToManyField(Team)
    match_date =  models.DateTimeField(blank = True)
    home_team_goals = models.IntegerField(default=0)  
    away_team_goals = models.IntegerField(default=0)    