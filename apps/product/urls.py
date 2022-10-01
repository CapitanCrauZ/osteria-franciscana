from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_product, name='list_product'),
    path('add/', views.add_product, name='add_product'),
    path('modify/<int:id>', views.modify_product, name='modify_product'),
    path('delete/<int:id>', views.delete_product, name='delete_product')
]