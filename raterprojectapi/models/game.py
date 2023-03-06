from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    release_date = models.DateField(null=True, blank=True, auto_now_add=False)
    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE)
