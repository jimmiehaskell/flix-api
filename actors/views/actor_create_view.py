from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Actor
    serializer_class = ActorSerializer
