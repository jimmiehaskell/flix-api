from rest_framework import generics

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateView(generics.CreateAPIView):
    model = Genre
    serializer_class = GenreSerializer