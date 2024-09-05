import matplotlib.pyplot as plt
import numpy as np

barangays = ["Abaca", "Bagumbayan", "Balzain", "Banila", "Biruk", "Canabay", "Carolotan", "Domang", "Dopaj", 
             "Gabut", "Ganao", "Kinabuan", "Kimbutan", "Lukidnon", "Mangayang", "Palabotan", "Sanguit", "Sta. Maria", "Talbek", "Total"]

years = ["2019", "2020", "2021", "2022", "2023"]

data = {
    "2019": [25, 128, 37, 51, 42, 60, 115, 101, 123, 61, 75, 101, 79, 53, 108, 167, 111, 79, 22, 1538],
    "2020": [25, 117, 38, 51, 30, 59, 115, 95, 111, 53, 80, 91, 80, 53, 104, 159, 92, 74, 29, 1456],
    "2021": [26, 98, 36, 46, 38, 53, 98, 81, 85, 42, 71, 78, 73, 47, 89, 140, 78, 72, 30, 1281],
    "2022": [22, 87, 29, 45, 38, 53, 86, 65, 70, 43, 64, 67, 61, 53, 74, 94, 69, 53, 29, 1102],
    "2023": [21, 73, 26, 45, 35, 52, 81, 61, 63, 36, 53, 60, 53, 51, 68, 84, 59, 51, 29, 1001]
}

bar_width = 0.15
index = np.arange(len(barangays))


plt.figure(figsize=(14, 8))
plt.bar(index, data["2019"], bar_width, label='2019', color='skyblue')
plt.bar(index + bar_width, data["2020"], bar_width, label='2020', color='orange')
plt.bar(index + 2*bar_width, data["2021"], bar_width, label='2021', color='green')
plt.bar(index + 3*bar_width, data["2022"], bar_width, label='2022', color='red')
plt.bar(index + 4*bar_width, data["2023"], bar_width, label='2023', color='purple')

plt.title('Number of Registered and Delinquent Business and Real Property Tax Payers By Barangay (2019-2023)', fontsize=16)
plt.xlabel('Barangay', fontsize=14)
plt.ylabel('Number of Tax Payers', fontsize=14)
plt.xticks(index + 2*bar_width, barangays, rotation=90)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
