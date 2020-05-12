from django.db import models


class CinemaAward(models.Model):
    name = models.CharField(max_length=255)
    movie_rank = models.ManyToManyField(
        'Movie',
        through='CinemaAwardMovie',
        verbose_name='cinema award movie',
        blank=True,
    )

    def __str__(self):
        return self.name


class CinemaAwardMovie(models.Model):
    cinema_award = models.ForeignKey(
        'CinemaAward', on_delete=models.CASCADE, verbose_name='cinema award'
    )
    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, verbose_name='movie'
    )
    rank = models.PositiveIntegerField()

    class Meta:
        unique_together = ('cinema_award', 'movie')

    def __str__(self):
        return '{}/{}'.format(self.cinema_award.name, self.movie.name)


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
