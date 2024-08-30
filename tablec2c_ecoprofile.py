import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
sources = [
    "Real Property Tax",
    "Tax on Business",
    "Other Taxes",
    "Regulatory Fees",
    "Service/User Charges",
    "Special Education Fund"
]

percentage_distribution = [
    9.10,  # Real Property Tax
    14.99,  # Tax on Business
    4.90,   # Other Taxes
    8.45,   # Regulatory Fees
    46.64,  # Service/User Charges
    11.31   # Special Education Fund
]

# Creating a histogram
plt.figure(figsize=(12, 8))
plt.bar(sources, percentage_distribution, color='skyblue')

# Adding titles and labels
plt.title('Percentage Distribution of Revenues and Receipts By Source (2019-2023)', fontsize=16)
plt.xlabel('Revenue Sources', fontsize=14)
plt.ylabel('Percentage (%)', fontsize=14)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
