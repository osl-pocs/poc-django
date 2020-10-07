from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import (
    ActorFactory,
    CastFactory,
    CinemaAwardFactory,
    CinemaAwardMovieFactory,
    MovieFactory,
    UserFactory,
)

# factory data


def get_new_cinema_award_instance(i=1):
    cinema_award = CinemaAwardFactory(name=f'cinema-award-{i}')
    movie1 = get_new_movie_instance(i=i * 10 + 1)['movie']
    movie2 = get_new_movie_instance(i=i * 10 + 2)['movie']

    movie_award1 = CinemaAwardMovieFactory(
        cinema_award=cinema_award, movie=movie1, rank=1
    )
    movie_award2 = CinemaAwardMovieFactory(
        cinema_award=cinema_award, movie=movie2, rank=1
    )

    return {
        'cinema_award': cinema_award,
        'rank': [movie_award1, movie_award2],
    }


def get_new_cinema_award_data(i=1):
    data = get_new_cinema_award_instance(i=i)

    return {
        'id': data['cinema_award'].id,
        'name': data['cinema_award'].name,
        'rank': [
            {
                'movie_id': v.movie.id,
                'movie_name': v.movie.name,
                'rank': v.rank,
            }
            for v in data['rank']
        ],
    }


def get_new_movie_instance(i=1):
    movie = MovieFactory(name=f'movie-{i}')
    actor1 = ActorFactory(name=f'actor-{i}-1')
    actor2 = ActorFactory(name=f'actor-{i}-2')

    casting_actor_1 = CastFactory(
        movie=movie, actor=actor1, character_name=f'character-name-{i}-1'
    )
    casting_actor_2 = CastFactory(
        movie=movie, actor=actor2, character_name=f'character-name-{i}-2'
    )

    return {'movie': movie, 'casting': [casting_actor_1, casting_actor_2]}


def get_new_movie_data(i=1):
    data = get_new_movie_instance(i=i)

    return {
        'id': data['movie'].id,
        'name': data['movie'].name,
        'casting': [
            {
                'actor_id': v.actor.id,
                'actor_name': v.actor.name,
                'character_name': v.character_name,
            }
            for v in data['casting']
        ],
    }


# test


class CinemaAPITestCase(APITestCase):
    URL_PREFIX_NAME = 'api:cinema'
    factory_class = MovieFactory

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

    def test_get_list(self):
        data = get_new_cinema_award_data()

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(f'{self.URL_PREFIX_NAME}-list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()['results'][0]
        assert result['name'] == data['name']
        assert result['rank'] == data['rank']

    def test_get_detail(self):
        data = get_new_cinema_award_data(i=1)

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(
                f'{self.URL_PREFIX_NAME}-detail', kwargs={'pk': data['id']}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()
        assert result['name'] == data['name']
        assert result['rank'] == data['rank']

    def test_get_cinema_movies_list(self):
        data = get_new_cinema_award_data(i=1)

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(f'{self.URL_PREFIX_NAME}-movies')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()
        assert result[0]['name'] == data['name']
        assert result[0]['rank'] == data['rank']

    def test_get_cinema_awards_by_movie(self):
        cinema1 = get_new_cinema_award_data(i=1)
        cinema2 = get_new_cinema_award_data(i=2)

        new_movie = CinemaAwardMovieFactory(
            cinema_award_id=cinema2['id'],
            movie_id=cinema1['rank'][0]['movie_id'],
            rank=3,
        )

        cinema2['rank'].append(
            {
                'movie_id': new_movie.movie.id,
                'movie_name': new_movie.movie.name,
                'rank': new_movie.rank,
            }
        )

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(
                f'{self.URL_PREFIX_NAME}-movies', kwargs={'movie_pk': 1}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()

        data = [cinema1, cinema2]

        assert len(data) == len(result)

        for i in range(len(result)):
            assert result[i]['name'] == data[i]['name']
            assert result[i]['rank'] == data[i]['rank']

    def test_put_cinema_awards_by_movie(self):
        cinema1 = get_new_cinema_award_data(i=1)

        self.client.force_authenticate(self.user)
        response = self.client.put(
            reverse_lazy(
                f'{self.URL_PREFIX_NAME}-movies',
                kwargs={'movie_pk': cinema1['id']},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
