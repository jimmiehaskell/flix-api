from rest_framework import generics, status
from rest_framework.response import Response

from movies.models import Movie


class MovieDeleteView(generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)