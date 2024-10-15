import pandas as pd

# Function to process the data
def process_scheduling_data(input_file, output_file):
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

    # Convert sorted equipment data into a DataFrame with equipment as columns
    max_rows = max([len(products) for products in sorted_equipment.values()])  # Find the maximum number of products for any equipment
    equipment_df = pd.DataFrame({eq: products + [None]*(max_rows - len(products)) for eq, products in sorted_equipment.items()})

    # Write the result to a new Excel file
    equipment_df.to_excel(output_file, index=False)

    print(f"Processed scheduling data has been saved to {output_file}")

# Example usage
input_csv_file = '/home/rajneel18/diabetes_products_single_sheet.csv'  # Path to your input CSV file
output_excel_file = 'output_scheduling_data.xlsx'  # Path where the output will be saved

process_scheduling_data(input_csv_file, output_excel_file)
