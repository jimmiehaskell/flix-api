from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from genres.models import Genre
from movies.models import Movie


class MovieUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        genre = Genre.objects.get(pk=request.data['genre'])
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)
        movie.title = request.data['title']
        movie.release_date = request.data['release_date']
        movie.resume = request.data['resume']
        movie.genre = genre
        movie.actors.set(request.data['actors'])
        movie.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'Movie updated successfully'
            }
        )
