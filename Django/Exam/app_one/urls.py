from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make),
    path('login', views.log_in),
    path('success', views.page_success), 
    path('logout', views.log_out), 
]