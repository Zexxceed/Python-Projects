import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
categories = ["Personal Services", "MOOE", "Capital Outlay", "Special Education Fund"]
years = ["2019", "2020", "2021", "2022", "2023"]

# Actual Expenditures by Item/Class of Expense
personal_services = [70641054.11, 69974533.97, 71444469.41, 78771847.73, 72532798.43]
mooe = [39978908.55, 56586220.58, 43349099.03, 81825036.55, 77161946.76]
capital_outlay = [22692983.62, 27599590.73, 19019067.47, 35805902.90, 37269312.91]
special_education_fund = [889689.50, 715260.72, 267349.45, 484056.00, 1031407.98]

# Bar width
bar_width = 0.2
index = np.arange(len(years))

# Create a bar plot
plt.figure(figsize=(14, 8))

plt.bar(index, personal_services, bar_width, label='Personal Services', color='skyblue')
plt.bar(index + bar_width, mooe, bar_width, label='MOOE', color='orange')
plt.bar(index + 2*bar_width, capital_outlay, bar_width, label='Capital Outlay', color='green')
plt.bar(index + 3*bar_width, special_education_fund, bar_width, label='Special Education Fund', color='red')

# Adding titles and labels
plt.title('Actual Expenditures By Item/Class of Expense (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + 1.5*bar_width, years)
plt.legend()

# Adding grid
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
