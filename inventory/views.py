from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from inventory.forms import ProductForm, IngredientForm
from upload.models import Product, Ingredient, Composition

#
# Actions for Products
#

@login_required
def display_products(request):
    products = Product.objects.all()
    return render(request, 'product/products.html', {'products': products})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('display_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('display_products')
    return render(request, 'product/confirm_delete_product.html', {'product': product})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_products')
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})

#
# Actions for Ingredients
#

@login_required
def display_ingredients(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient/ingredients.html', {'ingredients': ingredients})

@login_required
def edit_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, ingredient_id=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('display_ingredients')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient/edit_ingredient.html', {'form': form, 'ingredient': ingredient})

@login_required
def delete_ingredient(request, ingredient_id):
    ingredient = get_object_or_404(Ingredient, ingredient_id=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('display_ingredients')
    return render(request, 'ingredient/confirm_delete_ingredient.html', {'ingredient': ingredient})

@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_ingredients')
    else:
        form = IngredientForm()
    return render(request, 'ingredient/add_ingredient.html', {'form': form})


#
# Actions for Composition
#

@login_required
def display_composition(request):
    compositions = Composition.objects.all()
    return render(request, 'composition/composition.html', {'compositions': compositions})
