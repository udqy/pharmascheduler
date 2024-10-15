import pandas as pd
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Product, Ingredient, Composition
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required
import os

'''
@login_required
def upload_order(request):
    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location=settings.TEMP_UPLOAD_DIR)
            file_path = os.path.join(settings.TEMP_UPLOAD_DIR, filename)
            file_path = fs.path(file_path)
            
            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path)
                else:
                    raise ValueError("Invalid file format. Please upload a CSV or XLSX file.")

                for _, row in df.iterrows():
                    product_id = row['product_id']
                    product_name = row['product_name']
                    quantity = row['quantity']

                    # Get or create the product with the given ID and name
                    product, _ = Product.objects.update_or_create(
                        product_id=product_id,
                        defaults={'product_name': product_name}
                    )

                    # Create an Order with the fetched product and quantity
                    Order.objects.create(
                        product=product,
                        quantity=quantity
                    )

                os.remove(file_path)

                return redirect(next_url or 'success')
            except Exception as e:
                return render(request, 'upload.html', {
                    'form': form,
                    'error_message': str(e)
                })
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form, 'next': next_url})
'''

@login_required
def upload_products(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location=settings.TEMP_UPLOAD_DIR)
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.TEMP_UPLOAD_DIR, filename)

            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path)
                else:
                    raise ValueError("Invalid file format. Please upload a CSV or XLSX file.")

                for _, row in df.iterrows():
                    product_id = row['product_id']
                    product_name = row['product_name']
                    Product.objects.update_or_create(
                        product_id=product_id,
                        defaults={'product_name': product_name}
                    )

                os.remove(file_path)

                return redirect('success')
            except Exception as e:
                return render(request, 'upload_products.html', {
                    'form': form,
                    'error_message': str(e)
                })
    else:
        form = UploadFileForm()
    return render(request, 'upload_products.html', {'form': form})

@login_required
def upload_ingredients(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location=settings.TEMP_UPLOAD_DIR)
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.TEMP_UPLOAD_DIR, filename)

            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path)
                else:
                    raise ValueError("Invalid file format. Please upload a CSV or XLSX file.")

                for _, row in df.iterrows():
                    ingredient_id = row['ingredient_id']
                    ingredient_name = row['ingredient_name']
                    Ingredient.objects.update_or_create(
                        ingredient_id=ingredient_id,
                        defaults={'ingredient_name': ingredient_name}
                    )

                os.remove(file_path)

                return redirect('success')
            except Exception as e:
                return render(request, 'upload_ingredients.html', {
                    'form': form,
                    'error_message': str(e)
                })
    else:
        form = UploadFileForm()
    return render(request, 'upload_ingredients.html', {'form': form})

@login_required
def upload_composition(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage(location=settings.TEMP_UPLOAD_DIR)
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = os.path.join(settings.TEMP_UPLOAD_DIR, filename)

            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path)
                else:
                    raise ValueError("Invalid file format. Please upload a CSV or XLSX file.")

                for _, row in df.iterrows():
                    ingredient_id = row['ingredient_id']
                    product_id = row['product_id']
                    quantity = row['quantity']

                    ingredient = Ingredient.objects.get(ingredient_id=ingredient_id)
                    product = Product.objects.get(product_id=product_id)

                    Composition.objects.update_or_create(
                        ingredient=ingredient,
                        product=product,
                        defaults={'quantity': quantity}
                    )

                os.remove(file_path)

                return redirect('success')
            except Exception as e:
                return render(request, 'upload_composition.html', {
                    'form': form,
                    'error_message': str(e)
                })
    else:
        form = UploadFileForm()
    return render(request, 'upload_composition.html', {'form': form, 'title': 'Upload Composition'})