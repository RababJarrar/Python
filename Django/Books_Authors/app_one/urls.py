from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.addbook),
    path('books/<int:id>', views.bookdesc),
    path('add/<int:id>', views.selected_author),

    path('authors', views.index2),
    path('add_author', views.addauthor),
    path('authors/<int:id>', views.authordesc),
    path('add2/<int:id>', views.selected_book),
]
