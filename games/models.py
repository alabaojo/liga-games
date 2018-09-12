from django.db import models
from django.utils import timezone
#from django.db.models import Model, Manager

#from django.db.models import CharField, Model



class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    alias = models.CharField(max_length=60)
    

    def __str__(self):
        return self.name    

class Result(models.Model):
    home_goal = models.IntegerField()
    away_goal = models.IntegerField()



class Match(models.Model):
    teams = models.ManyToManyField(Team)
    match_order = models.IntegerField(default=0) 
    result = models.ForeignKey(Result, on_delete=models.CASCADE)

    class Meta:
        ordering = ('match_order',)

    def __str__(self):
        return self.match_order   
     

class Season(models.Model):
    start_date = models.DateTimeField(default= timezone.now(), blank=True)
    end_date = models.DateTimeField( default = timezone.now())
    matches = models.ManyToManyField(Match) 





