from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make_register),
    path('login', views.log),
    path('logout', views.out), 
    path('books', views.suc), 
    path('add_book/<int:id>', views.addbook),
    path('books/<int:id>', views.bookdetails),
    path('update_desc/<int:id>', views.updatedesc),
    path('delete_desc/<int:id>', views.deletedesc),
    path('un_fav/<int:idu>/<int:id>', views.unfavorite),
    path('fav/<int:idu>/<int:id>', views.favorite),
]