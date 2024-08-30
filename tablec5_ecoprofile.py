import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]

# Assets, Liabilities, and Equity data
assets = [335852198.20, 406058206.44, 435016084.76, 635340775.11, 684916201.50]
liabilities = [50697703.60, 79500958.04, 71184511.23, 105082893.67, 80763545.98]
equity = [285154494.60, 326557248.40, 363831573.53, 530257881.44, 604152655.52]

# Bar width
bar_width = 0.25
index = np.arange(len(years))

# Create a bar plot
plt.figure(figsize=(14, 8))

plt.bar(index, assets, bar_width, label='Assets', color='skyblue')
plt.bar(index + bar_width, liabilities, bar_width, label='Liabilities', color='orange')
plt.bar(index + 2*bar_width, equity, bar_width, label='Residual Equity', color='green')

# Adding titles and labels
plt.title('Comparative Presentation of Assets, Liabilities, and Residual Equities (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + bar_width, years)
plt.legend(fontsize="15")

# Adding grid
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
