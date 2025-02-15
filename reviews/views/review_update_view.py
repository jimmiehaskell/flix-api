from rest_framework import generics, status
from rest_framework.response import Response

from reviews.models import Review


class ReviewUpdateView(generics.RetrieveUpdateAPIView):
    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        review = Review.objects.get(pk=pk)
        review.comment = request.data['comment']
        review.rating = request.data['rating']
        review.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'Review updated successfully',
            }
        )
