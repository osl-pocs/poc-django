from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    casting = models.ManyToManyField(
        'Actor', through='Cast', verbose_name='casting', blank=True,
    )

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255)
    day_of_birth = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name


class Cast(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='movie'
    )
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, verbose_name='actor'
    )
    character_name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('movie', 'actor', 'character_name')

    def __str__(self):
        return '{}/{}/{}'.format(
            self.movie.name, self.actor.name, self.character_name
        )
