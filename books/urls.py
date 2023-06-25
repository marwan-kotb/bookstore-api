from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AuthorListCreateAPIView,
    BookListCreateAPIView,
    BookPageListCreateAPIView,
    BookPageRetrieveUpdateDestroyAPIView,
    BookRetrieveUpdateDestroyAPIView,
    PageListCreateAPIView,
    PageRetrieveUpdateDestroyAPIView,
    UserCreateAPIView,
)

urlpatterns = [
    path("authors/", AuthorListCreateAPIView.as_view(), name="author-list-create"),
    path("books/", BookListCreateAPIView.as_view(), name="book-list-create"),
    path(
        "books/<int:pk>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book-retrieve-update-destroy",
    ),
    path("pages/", PageListCreateAPIView.as_view(), name="page-list-create"),
    path(
        "pages/<int:pk>/",
        PageRetrieveUpdateDestroyAPIView.as_view(),
        name="page-retrieve-update-destroy",
    ),
    path(
        "book/<int:book>/pages/",
        BookPageListCreateAPIView.as_view(),
        name="book-page-list-create",
    ),
    path(
        "book/<int:book>/pages/<int:pk>",
        BookPageRetrieveUpdateDestroyAPIView.as_view(),
        name="book-page-retrieve-update-destroy",
    ),
    path("auth/token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("auth/register/", UserCreateAPIView.as_view(), name="user-create"),
]
