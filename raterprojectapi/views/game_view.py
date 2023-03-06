from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterprojectapi.models import Game, Gamer, Category

class GameView(ViewSet):
    """ This is the view for games """

    def retrieve(self, request, pk):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response ({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        games = Game.objects.all()
        
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
    def create(self, request):
            
            gamer = Gamer.objects.get(pk=request.data["gamer"])

            game = Game.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            release_date=request.data["release_date"],
            gamer=gamer
        )
            serializer = GameSerializer(game)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','title','description','release_date','gamer')
        depth = 1
