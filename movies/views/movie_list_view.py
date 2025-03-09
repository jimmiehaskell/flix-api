from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
