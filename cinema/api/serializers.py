from cinema.models import (
    Movie, Actor, Cast
)
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Movie Serializer."""
    casting = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['name', 'casting']


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    """Actor Serializer."""
    class Meta:
        model = Actor
        fields = ['name', 'day_of_birth']
