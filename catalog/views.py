from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Book, Author


class CatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request):
        books = Book.objects.all()

        params = {
            'title': "All",
            'books': books
        }

        return render(request, self.template_name, params)


class BookView(TemplateView):
    template_name = "catalog/book.html"

    def get(self, request, id):
        book = Book.objects.get(id=id)

        params = {
            'title': f"About {book.title}",
            'book': book
        }

        return render(request, self.template_name, params)


class AuthorsView(TemplateView):
    template_name = "catalog/authors.html"

    def get(self, request):
        authors = Author.objects.all()

        params = {
            'authors': authors
        }

        return render(request, self.template_name, params)


class AuthorCatalogView(TemplateView):
    template_name = "catalog/catalog.html"

    def get(self, request, first_name, last_name, id):
        author = Author.objects.get(id=id)
        books = Book.objects.filter(author=author)

        params = {
            'title': f"{last_name}'s",
            'author': author,
            'books': books
        }

        return render(request, self.template_name, params)


class SearchView(TemplateView):
    template_name = "catalog/catalog.html"

    def post(self, request):
        search = request.POST['search']
        books_by_filter = Book.objects.filter(title__icontains=search)| \
                Book.objects.filter(summary__icontains=search) | \
                Book.objects.filter(date_of_publication__icontains=search) | \
                Book.objects.filter(price__icontains=search) | \
                Book.objects.filter(author__last_name__icontains=search) | \
                Book.objects.filter(author__first_name__icontains=search)

        params = {
            'books': books_by_filter,
            'title': f"'{search}'"
        }

        return render(request, self.template_name, params)


