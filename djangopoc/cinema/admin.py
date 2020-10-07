from django.contrib import admin

from config.admin import admin_site
from djangopoc.cinema.models import (
    Actor,
    Cast,
    CinemaAward,
    CinemaAwardMovie,
    Movie,
)


class ActorAdmin(admin.ModelAdmin):
    ...


class CastAdmin(admin.ModelAdmin):
    ...


class CinemaAwardAdmin(admin.ModelAdmin):
    ...


class CinemaAwardMovieAdmin(admin.ModelAdmin):
    ...


class MovieAdmin(admin.ModelAdmin):
    ...


admin_site.register(Actor, ActorAdmin)
admin_site.register(Cast, CastAdmin)
admin_site.register(CinemaAward, CinemaAwardAdmin)
admin_site.register(CinemaAwardMovie, CinemaAwardMovieAdmin)
admin_site.register(Movie, MovieAdmin)
