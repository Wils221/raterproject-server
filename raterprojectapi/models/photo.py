from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):

    gamer = models.ForeignKey("gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("game", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images", height_field=None,width_field=None, max_length=None, null=True)
