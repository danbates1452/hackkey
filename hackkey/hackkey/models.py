# Database Models
from django.db import models
from uuid import uuid5 # for user_id

class Users(models.Model):
    user_id = models.IntegerField()
    email_address = models.EmailField()
    password = models.CharField()
    logged_in_today = models.BooleanField()
    login_daily_claimed = models.BooleanField()


class Entries(models.Model):
    entry_id = models.CharField()
    username = models.Charfield()
    password = models.CharField() #hashed
    uri = models.CharField() #todo: expand to having multiple URIs

