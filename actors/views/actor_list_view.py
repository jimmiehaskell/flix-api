from rest_framework import generics

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorListView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer