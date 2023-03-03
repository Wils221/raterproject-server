from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Rating(models.Model):

    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    review = models.CharField(max_length=500)
    date_created = models.DateField(null=True, blank=True, auto_now_add=True)
