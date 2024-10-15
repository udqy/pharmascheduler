from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_products, name='display_products'),
    path('products/', views.display_products, name='display_products'),
    path('ingredients/', views.display_ingredients, name='display_ingredients'),
    path('composition/', views.display_composition, name='display_composition'),
]