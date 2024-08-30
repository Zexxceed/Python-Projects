import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]
local_sources = [6607186.79, 7186377.13, 8157489.83, 7603906.04, 9643199.92]
external_sources = [184404001.52, 196228499.04, 194198709.96, 269612520.60, 230115046.10]
total_income = [191011188.31, 203414876.17, 202356199.79, 277216426.64, 239758246.02]
total_expenditures = [111489652.16, 126680601.27, 115020901.49, 161036240.28, 150726153.17]
non_income_receipts = [26326488.41, 29503514.61, 40667523.49, 38875136.60, 38279238.18]

# Positioning the bars
bar_width = 0.15
index = np.arange(len(years))

# Create a bar plot
plt.figure(figsize=(14, 8))

plt.bar(index, local_sources, bar_width, label='Local Sources')
plt.bar(index + bar_width, external_sources, bar_width, label='External Sources')
plt.bar(index + 2*bar_width, total_income, bar_width, label='Total Income')
plt.bar(index + 3*bar_width, total_expenditures, bar_width, label='Total Expenditures')
plt.bar(index + 4*bar_width, non_income_receipts, bar_width, label='Non-Income Receipts')

# Adding titles and labels
plt.title('Summary of Receipts and Expenditures for Dupax del Sur (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + 2*bar_width, years)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
