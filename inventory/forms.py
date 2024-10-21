from django import forms
from upload.models import Product, Ingredient, Composition

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name']

class CompositionForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
    quantity = forms.FloatField(min_value=0)

    class Meta:
        model = Composition
        fields = ['ingredient', 'quantity']