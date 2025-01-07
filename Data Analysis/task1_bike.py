import pandas as pd

# Load the data
file_path = 'C:\Users\Zexxceed\Desktop\Python Projects\Data Analysis\ebike_data.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Define replacements based on the provided criteria
# Replace missing values in categorical columns
categorical_replacements = {
    'bike_type': 'standard',
    'frame_material': 'unknown',
    'battery_type': 'other'
}

# Replace and clean categorical columns
for column, replacement in categorical_replacements.items():
    data[column] = data[column].str.lower().fillna(replacement)
    if column == 'bike_type':
        data[column] = data[column].apply(lambda x: x if x in ['standard', 'folding', 'mountain', 'road'] else 'standard')
    elif column == 'frame_material':
        data[column] = data[column].apply(lambda x: x if x in ['aluminum', 'steel', 'carbon fiber'] else 'unknown')
    elif column == 'battery_type':
        data[column] = data[column].apply(lambda x: x if x in ['li-ion', 'nimh', 'lead acid'] else 'other')

# Clean numeric columns that may contain non-numeric characters
data['motor_power'] = data['motor_power'].replace(regex=r'[^0-9.]', value='').astype(float)

# Define columns for missing value replacements using median and mean
median_columns = ['production_cost', 'motor_power']
mean_columns = ['assembly_time', 'top_speed', 'customer_score']

# Replace missing values in numeric columns with median and mean respectively
for column in median_columns:
    data[column] = data[column].fillna(data[column].median())
for column in mean_columns:
    data[column] = data[column].fillna(data[column].mean())

# Convert necessary columns to categorical dtype
categorical_columns = ['bike_type', 'frame_material', 'battery_type']
for column in categorical_columns:
    data[column] = data[column].astype('category')

# Final cleaned data
clean_data = data

# Display the cleaned data or save to a file
print(clean_data.head())  # To view the first few rows
clean_data.to_csv('cleaned_ebike_data.csv', index=False)  # Saves the cleaned data to a new CSV

