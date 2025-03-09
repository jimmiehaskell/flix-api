from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from actors.models import Actor


class ActorDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        actor = Actor.objects.get(pk=pk)
        actor.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={
                'message': 'Actor deleted',
            }
        )
