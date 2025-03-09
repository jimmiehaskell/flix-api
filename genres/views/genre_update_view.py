from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from genres.models import Genre


class GenreUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        genre = Genre.objects.get(pk=pk)
        genre.name = request.data['name']
        genre.save()
        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'Genre updated successfully'
            }
        )
