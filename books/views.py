from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Author, Book, Page
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    PageSerializer,
    UserSerializer,
)


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user

        author, created = Author.objects.get_or_create(user=user)

        serializer.save(author=author)


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookPageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        print(self.kwargs)
        book_id = self.kwargs["book"]
        return Page.objects.filter(book__id=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs["book"]
        book = Book.objects.get(id=book_id)
        serializer.save(book=book)


class BookPageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs["book"]
        return Page.objects.filter(book__id=book_id)

    def perform_create(self, serializer):
        book_id = self.kwargs["book"]
        book = Book.objects.get(id=book_id)
        serializer.save(book=book)


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token_serializer = TokenObtainPairSerializer()
        token_data = token_serializer.get_token(user=user)
        token = {
            "access_token": str(token_data.access_token),
            "refresh_token": str(token_data),
        }
        return Response({"user": serializer.data, "token": token})
