import pandas as pd

# Load Excel file
df = pd.read_excel('your_file.xlsx', sheet_name='Sheet1')

# Save as CSV
df.to_csv('your_file.csv', index=False)

