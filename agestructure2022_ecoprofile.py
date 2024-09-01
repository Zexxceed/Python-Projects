import matplotlib.pyplot as plt
import numpy as np

# Age group data
age_groups = [
    'Below 1 Yr', '1-4', '5-9', '10-14', '15-19', '20-24', '25-29', 
    '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', 
    '65-69', '70-74', '75-79', '80 & Above'
]

# Population data for 2022
males_2022 = [108, 685, 1030, 1060, 1070, 1085, 1070, 1030, 840, 780, 650, 625, 570, 425, 305, 185, 102, 98]
females_2022 = [117, 580, 860, 1010, 990, 975, 955, 865, 705, 635, 605, 575, 495, 385, 315, 215, 152, 148]

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
plt.legend()

# Adding grid
plt.grid(True, axis='x', linestyle='--', alpha=0.7)

# Display the plot
plt.show()
