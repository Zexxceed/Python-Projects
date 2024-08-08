import matplotlib.pyplot as plt
import numpy as np

# Data from the table
age_groups = [
    'Below 1 Yr', '1 – 4', '5 – 9', '10 – 14', '15 – 19', '20 – 24', '25 – 29', 
    '30 – 34', '35 – 39', '40 – 44', '45 – 49', '50 – 54', '55 – 59', '60 – 64', 
    '65 – 69', '70 – 74', '75 – 79', '80 & Above'
]
male_population = [108, 784, 1063, 1182, 1093, 1040, 1064, 996, 840, 731, 627, 644, 537, 404, 264, 165, 89, 100]
female_population = [119, 651, 992, 1053, 982, 1048, 925, 844, 654, 623, 576, 539, 454, 381, 293, 198, 139, 146]

# Convert male population to negative for population pyramid
male_population = [-val for val in male_population]

# Plotting the population pyramid
fig, ax = plt.subplots(figsize=(10, 8))

# Horizontal bar plots
ax.barh(age_groups, male_population, color='blue', label='Male')
ax.barh(age_groups, female_population, color='red', label='Female')

# Adding labels and title
ax.set_xlabel('Population')
ax.set_ylabel('Age')
ax.set_title('Population Pyramid (2021)')
ax.legend(prop={'size': 19})

# Setting the x-axis limit for better visualization
max_population = max(max(abs(np.array(male_population))), max(female_population))
ax.set_xlim(-max_population - 100, max_population + 100)

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Displaying the plot
plt.tight_layout()
plt.show()