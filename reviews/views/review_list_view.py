from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class ReviewListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
