from django.urls import path     
from . import views


urlpatterns = [
    path('shows', views.page_show),
    path('shows/new', views.page_add_show),
    path('create', views.create_show),
    path('shows/<int:id>', views.page_desc),
    path('shows/<int:id>/edit', views.page_edit),
    path('update/<int:id>', views.update_show),
    path('shows/<int:id>/destroy', views.delete_show),
]
