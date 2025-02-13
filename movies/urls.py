from django.urls import path

from movies.views import MovieListView, MovieCreateView, MovieDetailView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete', MovieDeleteView.as_view(), name='movie-delete'),
]