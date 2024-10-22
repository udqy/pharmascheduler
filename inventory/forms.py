from django import forms
from upload.models import Product, Ingredient, Composition, Equipment

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

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['equipment_name']

class UploadFileForm(forms.Form):
    file = forms.FileField()