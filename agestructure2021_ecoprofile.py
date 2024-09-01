import matplotlib.pyplot as plt
import numpy as np

# Age group data
age_groups = [
    'Below 1 Yr', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', 
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', 
    '65-69', '70-74', '75-79', '80 & Above'
]

# Population data for 2021
males_2021 = [108, 784, 1063, 1182, 1093, 1040, 1064, 996, 840, 731, 627, 644, 537, 404, 264, 165, 89, 100]
females_2021 = [119, 651, 992, 1053, 982, 1048, 925, 844, 654, 623, 576, 539, 454, 381, 293, 198, 139, 146]

# Create the plot for 2021
plt.figure(figsize=(10, 8))

# Create horizontal bar plots for males and females
bar_width = 0.4
index = np.arange(len(age_groups))

plt.barh(index, males_2021, bar_width, label='Males', color='blue')
plt.barh(index + bar_width, females_2021, bar_width, label='Females', color='lightblue')

# Adding titles and labels
plt.title('Age Structure of Dupax del Sur (2021)', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Age Group', fontsize=14)
plt.yticks(index + bar_width / 2, age_groups)
plt.legend(fontsize=15)

# Adding grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
