import matplotlib.pyplot as plt
import numpy as np

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]

# Income and Expenditure data
income = [168304647.80, 188991570.65, 202961010.18, 277704814.34, 241355763.79]
expenditure = [134202635.78, 154875606.00, 134079985.36, 196886843.18, 187995466.08]

# Bar width
bar_width = 0.35
index = np.arange(len(years))

# Create a bar plot
plt.figure(figsize=(14, 8))

plt.bar(index, income, bar_width, label='Income', color='skyblue')
plt.bar(index + bar_width, expenditure, bar_width, label='Expenditure', color='orange')

# Adding titles and labels
plt.title('Comparative Growth of Income and Expenditure for the Last Five Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + bar_width / 2, years)
plt.legend(fontsize="12")

# Adding grid
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
