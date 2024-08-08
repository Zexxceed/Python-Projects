import matplotlib.pyplot as plt
import numpy as np

# Data from the table
age_groups = [
    'Below 1 Yr', '1 – 4', '5 – 9', '10 – 14', '15 – 19', '20 – 24', '25 – 29', 
    '30 – 34', '35 – 39', '40 – 44', '45 – 49', '50 – 54', '55 – 59', '60 – 64', 
    '65 – 69', '70 – 74', '75 – 79', '80 & Above'
]
male_population = [105, 692, 1042, 1092, 1080, 1085, 1081, 1051, 849, 797, 656, 626, 577, 426, 312, 182, 103, 100]
female_population = [116, 574, 869, 1026, 993, 982, 956, 868, 709, 634, 615, 571, 498, 390, 319, 222, 151, 150]

# Convert male population to negative for population pyramid
male_population = [-val for val in male_population]

# Plotting the population pyramid
fig, ax = plt.subplots(figsize=(10, 8))

# Horizontal bar plots
ax.barh(age_groups, male_population, color='blue', label='Male')
ax.barh(age_groups, female_population, color='red', label='Female')

# Adding labels and title
ax.set_xlabel('Population')
ax.set_title('Population Pyramid (2023)')
ax.legend()

# Setting the x-axis limit for better visualization
max_population = max(max(abs(np.array(male_population))), max(female_population))
ax.set_xlim(-max_population - 100, max_population + 100)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Displaying the plot
plt.tight_layout()
plt.show()
