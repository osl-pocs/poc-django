from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import ActorFactory, CastFactory, MovieFactory, UserFactory


class CinemaAPITestCase(APITestCase):
    URL_PREFIX_NAME = 'api:cinema'
    factory_class = MovieFactory

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

    def get_new_data(self, i=1):
        movie = self.factory_class(name=f'movie-{i}')
        actor1 = ActorFactory(name=f'actor-{i}-1')
        actor2 = ActorFactory(name=f'actor-{i}-2')

        CastFactory(
            movie=movie, actor=actor1, character_name=f'character-name-{i}-1'
        )
        CastFactory(
            movie=movie, actor=actor2, character_name=f'character-name-{i}-2'
        )

        return {
            'id': movie.id,
            'name': f'movie-{i}',
            'casting': [
                {
                    'actor_name': f'actor-{i}-1',
                    'character_name': f'character-name-{i}-1',
                },
                {
                    'actor_name': f'actor-{i}-2',
                    'character_name': f'character-name-{i}-2',
                },
            ],
        }

    def test_list(self):
        data = self.get_new_data(1)

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(f'{self.URL_PREFIX_NAME}-list')
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.json()['results'][0]
        assert result['name'] == data['name']
        assert result['casting'] == data['casting']

    def test_detail(self):
        data = self.get_new_data()

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy(
                f'{self.URL_PREFIX_NAME}-detail', kwargs={'pk': data['id']}
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()

        assert result['name'] == data['name']
        assert result['casting'] == data['casting']
