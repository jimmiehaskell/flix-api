from rest_framework import generics

from genres.models import Genre
from genres.serializers import GenreSerializer


class ListGenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer