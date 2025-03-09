from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from reviews.models import Review
from reviews.serializers.review_serializer import ReviewSerializer


class ReviewCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Review
    serializer_class = ReviewSerializer
