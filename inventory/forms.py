from django import forms
from upload.models import Product, Ingredient, Composition, Equipment, EquipmentProductRelation

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

class EquipmentProductRelationForm(forms.ModelForm):
    equipment = forms.ModelChoiceField(
        queryset=Equipment.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
    )

    class Meta:
        model = EquipmentProductRelation
        fields = ['equipment']
