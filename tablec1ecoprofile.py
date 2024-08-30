import matplotlib.pyplot as plt

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]
local_sources = [6607186.79, 7186377.13, 8157489.83, 7603906.04, 9643199.92]
external_sources = [184404001.52, 196228499.04, 194198709.96, 269612520.60, 230115046.10]
total_income = [191011188.31, 203414876.17, 202356199.79, 277216426.64, 239758246.02]
total_expenditures = [111489652.16, 126680601.27, 115020901.49, 161036240.28, 150726153.17]
non_income_receipts = [26326488.41, 29503514.61, 40667523.49, 38875136.60, 38279238.18]

# Create a plot
plt.figure(figsize=(14, 8))

# Plotting each category
plt.plot(years, local_sources, marker='o', label='Local Sources')
plt.plot(years, external_sources, marker='o', label='External Sources')
plt.plot(years, total_income, marker='o', label='Total Income')
plt.plot(years, total_expenditures, marker='o', label='Total Expenditures')
plt.plot(years, non_income_receipts, marker='o', label='Non-Income Receipts')

# Adding titles and labels
plt.title('Summary of Receipts and Expenditures for Dupax del Sur (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
