from django.urls import path

from genres.views import GenreListView, GenreCreateView, GenreDetailView, \
    GenreDeleteView, GenreUpdateView

urlpatterns = [
    path('genres/', GenreListView.as_view(), name='movies_fk-list'),
    path('genres/create/', GenreCreateView.as_view(), name='movies_fk-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='movies_fk-detail'),
    path('genres/<int:pk>/delete', GenreDeleteView.as_view(), name='movies_fk-delete'),
    path('genres/<int:pk>/update', GenreUpdateView.as_view(), name='movies_fk-update'),
]
