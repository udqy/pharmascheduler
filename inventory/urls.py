from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products'),
    path('ingredients/', views.display_ingredients, name='display_ingredients'),
    path('composition/', views.display_composition, name='display_composition'),

    path('products/', views.display_products, name='display_products'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/add/', views.add_product, name='add_product'),
]