from django.urls import path

from genres.views import genre_create_list_view
from genres.views.genre_detail_view import genre_detail_view

urlpatterns = [
    path('genres/', genre_create_list_view, name='genre-create-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail'),
]
