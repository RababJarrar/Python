from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.addbook),
    path('books/<int:id>', views.bookdesc),
    path('add', views.selected_author),


]
