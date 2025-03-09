from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from actors.models import Actor
from actors.serializers import ActorSerializer


class ActorDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    lookup_field = 'pk'
