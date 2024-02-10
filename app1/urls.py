from django.urls import path
from .views import BookListCreateView, BookDetailView, ReviewCreateView,ReviewListView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews/list/', ReviewListView.as_view(), name='review-list'),  # Add this line for listing reviews
]
