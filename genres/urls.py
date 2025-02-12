from django.urls import path

from genres.views import GenreListView, GenreCreateView, GenreDetailView

urlpatterns = [
    path('genres/', GenreListView.as_view(), name='genre-list'),
    path('genres/create/', GenreCreateView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
]
