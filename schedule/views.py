import os
import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import ScheduleUploadForm
from .models import Schedule, Product

def process_scheduling_data(input_file):
    # Load CSV file
    df = pd.read_csv(input_file)

    # Define weights
    weight_quantity = 0.7
    weight_time = 0.3

    # Calculate combined score
    df['Score'] = (df['Quantity (Tons)'] / df['Completion Time (Days)']) * (weight_quantity + weight_time)

    # Create equipment lists
    equipment_lists = {}
    for index, row in df.iterrows():
        equipment = row['Equipment'].split(', ')
        for eq in equipment:
            if eq not in equipment_lists:
                equipment_lists[eq] = []
            equipment_lists[eq].append(row)

    # Sort products in each equipment list based on combined score
    sorted_equipment = {}
    for eq in equipment_lists:
        equipment_lists[eq] = sorted(equipment_lists[eq], key=lambda x: x['Score'], reverse=True)
        sorted_equipment[eq] = [product['Product Name'] for product in equipment_lists[eq]]

    # Convert sorted equipment data into a DataFrame
    max_rows = max([len(products) for products in sorted_equipment.values()])
    equipment_df = pd.DataFrame({eq: products + [None]*(max_rows - len(products)) for eq, products in sorted_equipment.items()})

    # Processed data can be stored as needed, e.g., into the Product model
    for eq, products in sorted_equipment.items():
        for i, product_name in enumerate(products):
            Product.objects.create(
                product_name=product_name,
                equipment_name=eq,
                phase='Phase 1' if 'Phase 1' in product_name else 'Phase 2',
                priority=i + 1
            )
    
    return equipment_df

def upload_schedule(request):
    if request.method == 'POST':
        form = ScheduleUploadForm(request.POST, request.FILES)
        if form.is_valid():
            schedule = form.save()
            input_file = schedule.schedule_file.path

            # Set the media path for saving the processed schedule
            media_path = os.path.join(settings.MEDIA_ROOT, 'processed_schedules')
            os.makedirs(media_path, exist_ok=True)  # Create the directory if it doesn't exist
            output_file = os.path.join(media_path, 'output.xlsx')

            # Process scheduling data and store in Product model
            equipment_df = process_scheduling_data(input_file)

            # Save the result as Excel file in the media folder
            equipment_df.to_excel(output_file, index=False)

            # Store the relative path to the media file in the model
            schedule.processed_file = 'processed_schedules/output.xlsx'
            schedule.save()

            return redirect('view_schedule', schedule_id=schedule.id)
    else:
        form = ScheduleUploadForm()
    return render(request, 'upload_schedule.html', {'form': form})

def view_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    products = Product.objects.all().order_by('priority')

    return render(request, 'view_schedule.html', {'schedule': schedule, 'products': products})
