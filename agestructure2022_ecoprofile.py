import matplotlib.pyplot as plt
import numpy as np

# Age group data
age_groups = [
    'Below 1 Yr', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', 
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', 
    '65-69', '70-74', '75-79', '80 & Above'
]

# Population data for 2022
males_2022 = [98, 745, 1046, 1145, 1090, 1061, 1059, 1067, 827, 813, 646, 650, 502, 433, 273, 170, 90, 107]
females_2022 = [85, 619, 931, 1051, 965, 980, 947, 870, 690, 653, 612, 522, 464, 391, 301, 203, 145, 152]

# Create the plot for 2022
plt.figure(figsize=(10, 8))

# Create horizontal bar plots for males and females
bar_width = 0.4
index = np.arange(len(age_groups))

plt.barh(index, males_2022, bar_width, label='Males', color='green')
plt.barh(index + bar_width, females_2022, bar_width, label='Females', color='lightgreen')

# Adding titles and labels
plt.title('Age Structure of Dupax del Sur (2022)', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Age Group', fontsize=14)
plt.yticks(index + bar_width / 2, age_groups)
plt.legend(fontsize=15)

# Adding grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
