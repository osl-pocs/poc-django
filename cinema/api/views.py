from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cinema.api.serializers import (
    ActorSerializer,
    CinemaAwardSerializer,
    MovieSerializer,
)
from cinema.models import Actor, CinemaAward, CinemaAwardMovie, Movie


class CinemaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = CinemaAward.objects.all().order_by('name')
    serializer_class = CinemaAwardSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path=r'',
        basename='cinema',
        url_name='movies',
    )
    def get_cinema_award_list(self, request, **kwargs):
        """
        Get a list of movies related to a cinema award.

        method: GET
        parameters:
          - cinema_award_pk: int
        return:
            [{
                "id": int,
                "name": int /* event ID */,
                /* example [{'id': 1, 'name': 'Into the Wild', 'rank': 1}] */
                "movies": [{'id': int, 'name': str, 'rank': int}]

            }, ... ]
        """
        instance = CinemaAward.objects.all()
        serializer = CinemaAwardSerializer(instance=instance, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path=r'(?P<cinema_award_pk>\d+)/movies/',
        basename='cinema',
        url_name='movies',
    )
    def get_cinema_award(self, request, cinema_award_pk):
        """
        Get a list of movies related to a cinema award.

        method: GET
        parameters:
          - cinema_award_pk: int
        return:
            {
                "id": int,
                "name": int /* event ID */,
                /* example [{'id': 1, 'name': 'Into the Wild', 'rank': 1}] */
                "movies": [{'id': int, 'name': str, 'rank': int}]

            }
        """
        instance = CinemaAward.objects.filter(id=int(cinema_award_pk))
        serializer = CinemaAwardSerializer(instance=instance, many=True)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=['get', 'put'],
        permission_classes=[IsAuthenticated],
        url_path=r'/movies/(?P<movie_pk>\d+)',
        basename='cinema',
        url_name='movies',
    )
    def get_cinema_award_by_movie(self, request, movie_pk: int):
        if request.method == 'GET':
            instance = CinemaAward.objects.filter(
                id__in=[
                    c.cinema_award.id
                    for c in CinemaAwardMovie.objects.filter(movie_id=1)
                ]
            )
            serializer = CinemaAwardSerializer(instance=instance, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


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
