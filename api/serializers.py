from rest_framework import serializers
from django.contrib.auth.models import User
from catalog.models import Book, Author, Genre
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['user', 'products', 'get_total_price', 'get_total_quantity']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Book
        fields = ['title', 'summary', 'date_of_publication', 'price', 'amount', 'book_cover', 'genre', 'author', 'get_genre', 'author_name']


class AuthorSerializer(serializers.ModelSerializer):
   # full_name = serializers.ReadOnlyField(source='author.get_full_name')

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        model = Author
        fields = ['get_full_name','first_name', 'last_name', 'date_of_birth', 'date_of_death', 'photo']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name', 'genre_picture']


