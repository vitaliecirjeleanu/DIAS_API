from django.db import models

class Results(models.Model):
    away_score = models.IntegerField()
    away_team = models.CharField()
    city = models.CharField()
    country = models.CharField()
    home_score = models.IntegerField()
    home_team = models.CharField()
    match_date = models.DateField()
    neutral = models.BooleanField()
    tournament = models.CharField()

class Goalscorers(models.Model):
    away_team = models.CharField()
    goal_team = models.CharField()
    home_team = models.CharField()
    match_date = models.DateField()
    minute = models.IntegerField()
    own_goal = models.BooleanField()
    penalty = models.BooleanField()
    scorer = models.CharField()

class Shootouts(models.Model):
    away_team = models.CharField()
    first_shooter = models.CharField()
    home_team = models.CharField()
    match_date = models.DateField()
    winner = models.CharField()
