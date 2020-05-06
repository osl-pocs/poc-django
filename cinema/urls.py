from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from cinema.api import views as api_views

from . import views

router = routers.DefaultRouter()
router.register(r'cinema', api_views.CinemaViewSet)
router.register(r'movies', api_views.MoviesViewSet)
router.register(r'actors', api_views.ActorViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/', include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^$', views.index, name='index'),
]
