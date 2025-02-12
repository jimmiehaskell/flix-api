from django.urls import path

from genres.views import ListGenreView
from genres.views.genre_detail_view import genre_detail_view

urlpatterns = [
    path('genres/', ListGenreView.as_view(), name='genre-list'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail'),
]
