from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	
    path('register', views.make),
    path('login', views.log_in),
    path('dashboard', views.page_success), 
    path('logout', views.log_out), 
    path('new/tree', views.page_add_tree), 
    path('add/<int:id>', views.add_tree), 
    path('user/account', views.show_tree),
    path('del/<int:id>', views.delete_tree),
    path('edit/<int:id>', views.page_edit_tree), 
    path('update/<int:id>', views.update_tree), 
    path('show/<int:id>', views.detailes),
]