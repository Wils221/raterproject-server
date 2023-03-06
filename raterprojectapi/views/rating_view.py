from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Rating, Gamer, Game

class RatingView(ViewSet):

    def update(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        rating.rating = request.data["rating"]
        rating.review = request.data["review"]
        rating.date_created = request.data["date_created"]

        game = Game.objects.get(pk=request.data["game"])
        rating.game = game

        gamer = Gamer.objects.get(pk=request.data["gamer"])
        rating.gamer = gamer
        rating.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)