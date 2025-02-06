import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre


@csrf_exempt
def genre_detail_view(request, pk) -> JsonResponse:
    genre = get_object_or_404(Genre, pk=pk)

    if request.method == 'GET':
        data = {
            'id': genre.id,
            'name': genre.name,
        }
        return JsonResponse(data, status=200)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse(
            data={
                'id': genre.id,
                'name': genre.name
            },
            status=201
        )

    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse(
            data={
                'message': 'Genre deleted'
            },
            status=204
        )