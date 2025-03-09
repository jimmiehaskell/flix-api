from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Movie
    serializer_class = MovieSerializer
