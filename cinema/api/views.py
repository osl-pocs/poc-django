from rest_framework import viewsets
from rest_framework import permissions
from cinema.models import (Movie, Actor, Cast)
from cinema.api.serializers import (
    MovieSerializer, ActorSerializer
)


class CinemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all().order_by('-date_joined')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]

class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]
