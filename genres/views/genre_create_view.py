from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Genre
    serializer_class = GenreSerializer
