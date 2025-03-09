from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from reviews.models import Review


class ReviewDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        review = Review.objects.get(pk=pk)
        review.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={
                'message': 'Review as been deleted.',
            }
        )
