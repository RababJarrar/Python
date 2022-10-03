from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make),
    path('login', views.log),
    path('success', views.suc), 
    path('logout', views.suc2),    
]
