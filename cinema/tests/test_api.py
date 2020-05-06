from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase

from .factory import MovieFactory, UserFactory


class CinemaAPITestCase(APITestCase):
    URL_PREFIX_NAME = 'api:cinema'
    factory_class = MovieFactory

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()

    def get_new_data(self, i=1):
        self.factory_class(name='username={i}')

        return {
            "name": f"username-{i}",
        }

    def test_list(self):
        data = self.factory_class()

        self.client.force_authenticate(self.user)
        response = self.client.get(
            reverse_lazy('{}-list'.format(self.URL_PREFIX_NAME))
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        result = response.data["results"][0]

        assert result['name'] == data.name
        assert result['casting'] == [v.name for v in data.casting.all()]
