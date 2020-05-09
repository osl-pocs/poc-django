from rest_framework import serializers

from cinema.models import Actor, Cast, Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """Movie Serializer."""

    casting = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['name', 'casting']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'casting': [
                {
                    'actor_name': v.actor.name,
                    'character_name': v.character_name,
                }
                for v in Cast.objects.filter(movie_id=instance.id)
            ],
        }


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    """Actor Serializer."""

    class Meta:
        model = Actor
        fields = ['name', 'day_of_birth']
