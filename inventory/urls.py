from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products'),
    path('composition/', views.display_composition, name='display_composition'),

    path('ingredients/', views.display_ingredients, name='display_ingredients'),
    path('ingredients/edit/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    path('ingredients/delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('ingredients/add/', views.add_ingredient, name='add_ingredient'),

    path('products/', views.display_products, name='display_products'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/add/', views.add_product, name='add_product'),
]