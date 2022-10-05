from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make_register),
    path('login', views.log_in),
    path('logout', views.log_out),
    path('success', views.show_main_page), 
 
]