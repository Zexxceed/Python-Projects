import matplotlib.pyplot as plt
import numpy as np

# Age group data
age_groups = [
    'Below 1 Yr', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', 
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', 
    '65-69', '70-74', '75-79', '80 & Above'
]

# Population data for 2023
males_2023 = [105, 692, 1042, 1092, 1080, 1085, 1081, 1051, 849, 797, 656, 626, 577, 426, 312, 182, 103, 100]
females_2023 = [116, 574, 869, 1026, 993, 982, 956, 868, 709, 634, 615, 571, 498, 390, 319, 222, 151, 150]

# Create the plot for 2023
plt.figure(figsize=(10, 8))

# Create horizontal bar plots for males and females
bar_width = 0.4
index = np.arange(len(age_groups))

plt.barh(index, males_2023, bar_width, label='Males', color='purple')
plt.barh(index + bar_width, females_2023, bar_width, label='Females', color='pink')

# Adding titles and labels
plt.title('Age Structure of Dupax del Sur (2023)', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Age Group', fontsize=14)
plt.yticks(index + bar_width / 2, age_groups)
plt.legend()

# Adding grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
