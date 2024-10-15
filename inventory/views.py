from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from upload.models import Product, Ingredient, Composition

@login_required
def display_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def display_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients': ingredients})

@login_required
def display_composition(request):
    compositions = Composition.objects.all()
    return render(request, 'composition.html', {'compositions': compositions})