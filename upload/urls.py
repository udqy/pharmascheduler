from django.urls import path
from . import views

urlpatterns = [
    #path('', views.upload_order, name='upload_file'),
    path('products/', views.upload_products, name='upload_products'),
    path('ingredients/', views.upload_ingredients, name='upload_ingredients'),
    path('composition/', views.upload_composition, name='upload_composition'),
]