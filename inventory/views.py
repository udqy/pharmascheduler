from django.forms import formset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from inventory.forms import CompositionForm, ProductForm, IngredientForm, EquipmentForm
from upload.models import Product, Ingredient, Composition, Equipment

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
    CompositionFormSet = formset_factory(CompositionForm, extra=1)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        formset = CompositionFormSet(request.POST, prefix='compositions')
        
        if form.is_valid() and formset.is_valid():
            form.save()
            
            # Get existing compositions for this product
            existing_compositions = {(c.ingredient_id, c.product_id): c for c in Composition.objects.filter(product=product)}
            
            for composition_form in formset:
                if composition_form.cleaned_data:
                    ingredient = composition_form.cleaned_data['ingredient']
                    quantity = composition_form.cleaned_data['quantity']
                    
                    # Check if this composition already exists
                    key = (ingredient.ingredient_id, product.product_id)
                    if key in existing_compositions:
                        # Update existing composition
                        composition = existing_compositions[key]
                        composition.quantity = quantity
                        composition.save()
                        del existing_compositions[key]
                    else:
                        # Create new composition
                        Composition.objects.create(
                            product=product,
                            ingredient=ingredient,
                            quantity=quantity
                        )
            
            return redirect('display_products')
    else:
        form = ProductForm(instance=product)
        compositions = Composition.objects.filter(product=product)
        formset = CompositionFormSet(initial=[
            {'ingredient': c.ingredient, 'quantity': c.quantity} for c in compositions
        ], prefix='compositions')
    
    return render(request, 'product/edit_product.html', {
        'form': form,
        'formset': formset,
        'product': product
    })

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
# For Composition
#
def delete_composition(request, product_id, ingredient_id):
    if request.method == 'POST':
        composition = get_object_or_404(Composition, product_id=product_id, ingredient_id=ingredient_id)
        composition.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


#
# For equipments
#

@login_required
def display_equipments(request):
    equipments = Equipment.objects.all()
    return render(request, 'equipment/equipments.html', {'equipments': equipments})

@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_equipments')
    else:
        form = EquipmentForm()
    return render(request, 'equipment/add_equipment.html', {'form': form})

@login_required
def edit_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, equipment_id=equipment_id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('display_equipments')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment/edit_equipment.html', {'form': form, 'equipment': equipment})

@login_required
def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, equipment_id=equipment_id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('display_equipments')
    return render(request, 'equipment/confirm_delete_equipment.html', {'equipment': equipment})