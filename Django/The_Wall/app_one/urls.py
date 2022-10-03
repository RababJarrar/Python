from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make),
    path('login', views.log),
    path('success', views.suc), 
    path('logout', views.out), 
    path('postmessage/<int:id>', views.post_m),
    path('postcomment/<int:u_id>/<int:m_id>', views.post_c),     
]
