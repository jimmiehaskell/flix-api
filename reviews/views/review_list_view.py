from rest_framework import generics

from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
