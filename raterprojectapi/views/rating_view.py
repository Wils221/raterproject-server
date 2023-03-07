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

    """Gamer rater game ratings & reviews view"""

    def retrieve(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game ratings
        Returns:
            Response -- JSON serialized list of game ratings
        """
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """

        #getting the user that is logged in 
        gamer = Gamer.objects.get(user=request.auth.user)
        #retrieve game from database. make sure the game the user is trying to add with the new rating actually exists in database  
        game = Game.objects.get(pk=request.data["game"])

        # whichever keys are used on the request.data must match what the client is passing to the server.
        rating = Rating.objects.create(
            rating=request.data["rating"],
            review=request.data["review"],
            date_created=request.data["date_created"],
            gamer=gamer, 
            game =game
        )
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

class RatingGamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ( 'full_name', )

class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for game ratings"""

    gamer = RatingGamerSerializer()

    class Meta:
        model = Rating
        fields = ( 'id', 'gamer', 'game', 'rating', 'review', 'date_created',)
