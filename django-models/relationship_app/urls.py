from django.urls import path

from .views import (LibraryDetailView, LoginView, LogoutView, RegisterView,
                    admin_view, librarian_view, list_books, member_view)

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login'),),
    path('logout/', LogoutView.as_view(template_name='logout'),),
    path('register/', RegisterView.views.register(), name='register'),
]
