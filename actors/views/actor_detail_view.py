from rest_framework import generics

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'pk'