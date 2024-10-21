from django import forms
from upload.models import Product, Ingredient

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name']