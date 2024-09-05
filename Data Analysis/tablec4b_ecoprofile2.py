import matplotlib.pyplot as plt
import numpy as np

categories = [
    "General Public Services", "Education Culture & Sports", "Health Nutrition & Population Control",
    "Housing and Community Development", "Social Services and Social Welfare", "Economic Services"
]

years = ["2019", "2020", "2021", "2022", "2023"]

general_public_services = [76636965.58, 96770155.37, 80032112.51, 112224693.09, 96467019.00]
education_culture_sports = [889689.50, 715260.72, 267349.45, 484056.00, 1031407.98]
health_nutrition_population = [11117093.90, 14168789.07, 11620742.24, 17764551.24, 16772440.89]
housing_community_development = [0, 0, 2952968.87, 0, 2121632.44]
social_services_welfare = [9862150.11, 3744468.69, 4562207.54, 14897855.92, 18893983.17]
economic_services = [35696736.69, 39476932.15, 34644604.75, 51515686.93, 52708982.60]

bar_width = 0.15
index = np.arange(len(years))

plt.figure(figsize=(14, 8))

plt.bar(index, general_public_services, bar_width, label='General Public Services', color='skyblue')
plt.bar(index + bar_width, education_culture_sports, bar_width, label='Education Culture & Sports', color='orange')
plt.bar(index + 2*bar_width, health_nutrition_population, bar_width, label='Health Nutrition & Population Control', color='green')
plt.bar(index + 3*bar_width, housing_community_development, bar_width, label='Housing & Community Development', color='red')
plt.bar(index + 4*bar_width, social_services_welfare, bar_width, label='Social Services & Welfare', color='purple')
plt.bar(index + 5*bar_width, economic_services, bar_width, label='Economic Services', color='brown')
plt.title('Total Expenditure By Function/Service (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + 2.5*bar_width, years)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize="8")
plt.show()
