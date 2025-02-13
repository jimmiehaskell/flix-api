from rest_framework import generics

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorCreateView(generics.CreateAPIView):
    model = Actor
    serializer_class = ActorSerializer