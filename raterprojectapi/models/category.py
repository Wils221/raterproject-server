from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    label = models.CharField(max_length=40)
