from django.urls import path

from .views import (LibraryDetailView, LoginView, LogoutView, RegisterView,
                    list_books)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login'),),
    path('logout/', LogoutView.as_view(template_name='logout'),),
    path('register/', RegisterView.views.register(), name='register'),
]
