from django.urls import path

from reviews.views import ReviewCreateView, ReviewDeleteView, ReviewDetailView, \
    ReviewListView, ReviewUpdateView

urlpatterns = [
    path(
        route='reviews/create',
        view=ReviewCreateView.as_view(),
        name='review-create'
    ),
    path(
        route='reviews/<int:pk>/delete',
        view=ReviewDeleteView.as_view(),
        name='review-delete'
    ),
    path(
        route='reviews/<int:pk>',
        view=ReviewDetailView.as_view(),
        name='review-detail'
    ),
    path(
        route='reviews',
        view=ReviewListView.as_view(),
        name='review-list'
    ),
    path(
        route='reviews/<int:pk>/update',
        view=ReviewUpdateView.as_view(),
        name='review-update'
    ),
]
