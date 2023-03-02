from django.db import models
from django.contrib.auth.models import User


class GameCategory(models.Model):

    categories = models.ForeignKey("category", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)
