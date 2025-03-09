from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'pk'
