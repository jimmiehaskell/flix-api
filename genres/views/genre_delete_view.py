from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from genres.models import Genre


class GenreDeleteView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        genre = Genre.objects.get(id=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
