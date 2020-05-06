from rest_framework import permissions, viewsets

from cinema.api.serializers import ActorSerializer, MovieSerializer
from cinema.models import Actor, Movie


class CinemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """

    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """

    queryset = Actor.objects.all().order_by('name')
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]
