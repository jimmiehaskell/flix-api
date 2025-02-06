from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from genres.models import Genre


@csrf_exempt
def genre_detail_view(request, pk) -> JsonResponse:
    genre = get_object_or_404(Genre, pk=pk)
    data = {
        'id': genre.id,
        'name': genre.name,
    }
    return JsonResponse(data, status=200)