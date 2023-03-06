from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Gamer

class gameView(ViewSet):
    """ This is the view for games """

#UPDATE 
    def update(self, request, pk):
        """Handle PUT requests for a game
        Returns:
            Response -- Empty body with 204 status code 
        """
        game = Game.objects.get(pk=pk)

        game.title = request.data["title"]
        game.description = request.data["description"]
        game.release_date = request.data["release_date"]

        gamer = Gamer.objects.get(pk=request.data["organizer"])
        game.gamer = gamer

        game.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)