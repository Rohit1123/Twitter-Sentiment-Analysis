# from itertools import twitter_account
from django.db import models

class Twitter_account(models.Model):
    name = models.CharField(max_length=128)
    hash_tag = models.CharField(max_length=1024)

    def __str__(self):
         return self.name

class Tweet(models.Model):
    twitter_account = models.CharField(max_length=128)
    tweet = models.CharField(max_length=1024)
    date = models.DateField('tweet date')
    hash_tag = models.CharField(max_length=1024)

    def __str__(self):
         return self.tweet