from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

def hello_view(request):
    return JsonResponse({
        'hello': 'Hello World!'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_view),
]
