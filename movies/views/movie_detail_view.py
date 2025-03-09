from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'
