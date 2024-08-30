import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]
local_sources = [6607186.79, 7186377.13, 8157489.83, 7603906.04, 9643199.92]
ira_share = [161007840.00, 181133999.04, 194133546.00, 269366099.04, 230046612.00]

# Creating the bar width
bar_width = 0.35
index = np.arange(len(years))

# Creating the bar plot
plt.figure(figsize=(14, 8))

plt.bar(index, local_sources, bar_width, label='Locally Generated Revenues', color='skyblue')
plt.bar(index + bar_width, ira_share, bar_width, label='IRA Share', color='orange')

# Adding titles and labels
plt.title('Comparative Presentation of Locally Generated Revenues vs. IRA Share (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + bar_width / 2, years)
plt.legend()

# Adding grid
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
