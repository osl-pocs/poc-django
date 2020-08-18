import datetime

import factory
from django.contrib.auth.models import User
from django.utils import timezone

from djangopoc.cinema.models import (
    Actor,
    Cast,
    CinemaAward,
    CinemaAwardMovie,
    Movie,
)


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'username-{n+1}')
    password = 'password'

    class Meta:
        model = User


class CinemaAwardFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'cinema-award-{n+1}')

    class Meta:
        model = CinemaAward


class MovieFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'movie-name-{n+1}')

    class Meta:
        model = Movie


class CinemaAwardMovieFactory(factory.django.DjangoModelFactory):
    cinema_award = factory.SubFactory(CinemaAwardFactory)
    movie = factory.SubFactory(MovieFactory)

    class Meta:
        model = CinemaAwardMovie


class ActorFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: f'actor-name-{n+1}')
    day_of_birth = factory.LazyFunction(
        lambda: timezone.now() - datetime.timedelta(weeks=20 * 52)
    )

    class Meta:
        model = Actor


class CastFactory(factory.django.DjangoModelFactory):
    movie = factory.SubFactory(MovieFactory)
    actor = factory.SubFactory(ActorFactory)
    character_name = factory.Sequence(lambda n: f'character-name-{n+1}')

    class Meta:
        model = Cast
