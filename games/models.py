from django.db import models

from django.db.models import CharField, Model

class Team(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    stadium = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Fixture(models.Model):
    match_order = models.IntegerField(default=0) 
    match_date =  models.DateTimeField(blank = True)
    #home_team = models.ForeignKey(Team, on_delete=models.PROTECT)
    #away_team = models.ForeignKey(Team, on_delete=models.PROTECT)
    result = models.IntegerField(default=0)  
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)

    class Meta:
        ordering = ('team_id',)

    def __str__(self):
        return self.match_order 
    
class Season(models.Model):
    start_date = models.DateTimeField()
    start_date = models.DateTimeField()
    team_id = models.ForeignKey(Team, on_delete=models.PROTECT)


