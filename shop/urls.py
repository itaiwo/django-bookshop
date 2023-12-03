from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("books/", views.books),
    path("books/<int:id>", views.books_by_id),
    path("books/<str:author>", views.books_by_author),
    path("books/",views.add_book)
    
]