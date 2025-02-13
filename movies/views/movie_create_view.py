from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateView(generics.CreateAPIView):
    model = Movie
    serializer_class = MovieSerializer
