from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products'),
    
    path('ingredients/', views.display_ingredients, name='display_ingredients'),
    path('ingredients/edit/<int:ingredient_id>/', views.edit_ingredient, name='edit_ingredient'),
    path('ingredients/delete/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
    path('ingredients/add/', views.add_ingredient, name='add_ingredient'),

    path('products/', views.display_products, name='display_products'),
    path('products/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/delete-composition/<int:ingredient_id>/', views.delete_composition, name='delete_composition'),
    path('products/<int:product_id>/delete-equipment/<int:equipment_id>/', views.delete_equipment_relation, name='delete_equipment_relation'),

    path('equipment/', views.display_equipments, name='display_equipments'),
    path('equipment/edit/<int:equipment_id>/', views.edit_equipment, name='edit_equipment'),
    path('equipment/delete/<int:equipment_id>/', views.delete_equipment, name='delete_equipment'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
]