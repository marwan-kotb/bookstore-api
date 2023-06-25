from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Author, Book, Page


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "user", "bio"]


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.user.username")

    class Meta:
        model = Book
        fields = ["id", "title", "author", "description"]


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ["id", "book", "number", "content"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )
        return user
