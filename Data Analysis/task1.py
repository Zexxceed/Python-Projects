import pandas as pd

# Step 1: Load the data
try:
    df = pd.read_csv('C:\Users\Zexxceed\Desktop\Python Projects\Data Analysis\production_data.csv')
except FileNotFoundError:
    print("File not found. Please check the file path.")
    raise

# Step 2: Handle missing values
# Replace missing 'raw_material_supplier' with 'national_supplier'
df['raw_material_supplier'].fillna('national_supplier', inplace=True)

# Replace missing 'pigment_type' with 'other'
df['pigment_type'].fillna('other', inplace=True)

# Replace missing 'pigment_quantity' with the median of the column
df['pigment_quantity'].fillna(df['pigment_quantity'].median(), inplace=True)

# Replace missing 'mixing_time' with the mean of the column
df['mixing_time'].fillna(df['mixing_time'].mean(), inplace=True)

# Replace missing 'mixing_speed' with 'Not Specified'
df['mixing_speed'].fillna('Not Specified', inplace=True)

# Replace missing 'product_quality_score' with the mean of the column
df['product_quality_score'].fillna(df['product_quality_score'].mean(), inplace=True)

# Step 3: Convert data types
# Check for missing values in 'batch_id' and remove those before converting to integer
df['batch_id'] = df['batch_id'].dropna().astype(int)

# Convert 'production_date' to datetime, handle errors gracefully
df['production_date'] = pd.to_datetime(df['production_date'], errors='coerce')

# Convert 'raw_material_supplier' and 'pigment_type' to categorical
df['raw_material_supplier'] = df['raw_material_supplier'].astype('category')
df['pigment_type'] = df['pigment_type'].astype('category')

# Clean categorical data by standardizing text cases, ensure proper type conversion
df['raw_material_supplier'] = df['raw_material_supplier'].astype(str).str.lower().str.replace('_', ' ')
df['pigment_type'] = df['pigment_type'].astype(str).str.lower()

# Output the cleaned data
clean_data = df
print(clean_data)
