import pandas as pd
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Order, Product
from .forms import UploadFileForm
from django.contrib.auth.decorators import login_required

@login_required
def upload_file(request):
    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            fs = FileSystemStorage()
            file_path = fs.save(uploaded_file.name, uploaded_file)
            file_full_path = fs.path(file_path)
            
            # Check the file type and process accordingly
            if file_full_path.endswith('.csv'):
                df = pd.read_csv(file_full_path)
            elif file_full_path.endswith('.xlsx'):
                df = pd.read_excel(file_full_path)
                csv_file_path = file_full_path.replace('.xlsx', '.csv')
                df.to_csv(csv_file_path, index=False)

            # Process the DataFrame and add it to the database
            for _, row in df.iterrows():
                product_name = row['product_name']
                quantity = row['quantity']

                # Fetch the product by name from the Product table
                try:
                    product = Product.objects.get(product_name=product_name)
                except Product.DoesNotExist:
                    # Handle the case where the product doesn't exist (raise error or create)
                    return render(request, 'upload.html', {
                        'form': form,
                        'error_message': f"Product '{product_name}' does not exist in the database."
                    })

                # Create an Order with the fetched product and quantity
                Order.objects.create(
                    product=product,
                    quantity=quantity
                )

            return redirect(next_url or 'success')  # Redirect to success or next URL
    else:
        form = UploadFileForm()

    return render(request, 'upload.html', {'form': form, 'next': next_url})
