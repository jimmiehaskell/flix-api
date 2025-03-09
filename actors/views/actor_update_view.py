from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from actors.models import Actor


class ActorUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        actor = Actor.objects.get(pk=pk)
        actor.name = request.data['name']
        actor.birthday = request.data['birthday']
        actor.nationality = request.data['nationality']
        actor.save()

        return Response(
            status=status.HTTP_200_OK,
            data={
                'message': 'Actor updated successfully'
            }
        )
