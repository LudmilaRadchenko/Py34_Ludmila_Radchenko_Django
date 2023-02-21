
from django.urls import path
from .views import UserList, BookList, GenreList, AuthorList, CartList, UserDetail, BookDetail, AuthorDetail, GenreDetail, CartDetail


urlpatterns = [
    path('users/', UserList.as_view(), name="api-users"),
    path('users/<int:pk>/', UserDetail.as_view(), name="api-user-detail"),
    path('books/', BookList.as_view(), name="api-books"),
    path('books/<int:pk>/', BookDetail.as_view(), name="api-book-detail"),
    path('genres/', GenreList.as_view(), name="api-genres"),
    path('genres/<int:pk>/', GenreDetail.as_view(), name="api-genre-detail"),
    path('authors/', AuthorList.as_view(), name="api-authors"),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name="api-author-detail"),
    path('carts/', CartList.as_view(), name="api-carts"),
    path('carts/<int:pk>/', CartDetail.as_view(), name="api-cart-detail"),
]