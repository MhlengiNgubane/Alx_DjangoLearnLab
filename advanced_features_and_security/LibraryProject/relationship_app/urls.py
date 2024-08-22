from django.urls import path

from .views import (LibraryDetailView, LoginView, LogoutView, RegisterView,
                    add_book, admin_view, delete_book, edit_book,
                    librarian_view, list_books, member_view)

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login'),),
    path('logout/', LogoutView.as_view(template_name='logout'),),
    path('register/', RegisterView.views.register(), name='register'),
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book<int:book_id>/', delete_book, name='delete_book'),
]
