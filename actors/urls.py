from django.urls import path

from actors.views import ActorListView, ActorCreateView, ActorUpdateView, ActorDetailView, ActorDeleteView

urlpatterns = [
    path('actors/', ActorListView.as_view(), name='actor-list'),
    path('actors/create/', ActorCreateView.as_view(), name='actor-create'),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name='actor-detail'),
    path('actors/<int:pk>/update', ActorUpdateView.as_view(), name='actor-update'),
    path('actors/<int:pk>/delete', ActorDeleteView.as_view(), name='actor-delete'),
]
