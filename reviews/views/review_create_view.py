from rest_framework import generics

from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    model = Review
    serializer_class = ReviewSerializer
