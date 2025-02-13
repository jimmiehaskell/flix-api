from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer