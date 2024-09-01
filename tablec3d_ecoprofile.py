import matplotlib.pyplot as plt
import numpy as np

barangays = [
    "Abaca", "Bagumbayan", "Balzain", "Banila", "Biruk", "Canabay", "Carolotan",
    "Domang", "Dopaj", "Gabut", "Ganao", "Kinabuan", "Kimbutan", "Lukidnon", 
    "Mangayang", "Palabotan", "Sanguit", "Sta. Maria", "Talbek"
]

years = ["2019", "2020", "2021", "2022", "2023"]

data = {
    "2019": [73877.59, 562518.22, 181551.43, 297918.06, 254769.53, 467488.31, 959703.53, 539325.83, 391801.94, 
             257957.76, 433041.40, 519333.11, 184377.23, 183713.77, 349177.10, 534560.45, 223634.90, 143221.95, 81380.57],
    "2020": [82914.10, 545386.21, 213395.26, 318867.03, 270361.73, 501697.96, 584251.64, 482456.75, 456285.52, 
             276285.42, 485127.66, 553286.35, 208576.54, 202216.90, 353892.31, 617112.32, 209682.51, 160335.28, 90749.76],
    "2021": [54346.80, 323269.45, 148129.40, 180032.80, 163556.20, 294802.20, 374636.30, 328586.38, 250791.28, 
             160848.56, 276498.84, 333020.86, 122845.20, 120907.00, 196637.60, 366229.80, 147629.48, 119305.26, 61749.60],
    "2022": [59219.40, 334767.89, 137200.20, 193290.00, 158807.40, 298029.60, 379296.10, 294005.98, 247194.00, 
             182341.96, 275583.84, 329255.66, 123268.00, 168689.00, 226812.40, 419906.60, 161342.20, 102049.25, 67881.80],
    "2023": [63543.00, 268292.09, 135838.20, 198446.80, 164936.80, 313702.00, 403569.90, 318479.38, 244078.32, 
             185208.56, 263669.44, 299135.26, 115142.40, 173264.40, 216859.60, 352073.20, 156983.00, 87928.05, 73625.40]
}

bar_width = 0.15
index = np.arange(len(barangays))

plt.figure(figsize=(14, 8))

plt.bar(index, data["2019"], bar_width, label='2019', color='skyblue')
plt.bar(index + bar_width, data["2020"], bar_width, label='2020', color='orange')
plt.bar(index + 2*bar_width, data["2021"], bar_width, label='2021', color='green')
plt.bar(index + 3*bar_width, data["2022"], bar_width, label='2022', color='red')
plt.bar(index + 4*bar_width, data["2023"], bar_width, label='2023', color='purple')

plt.title('Inventory of Other Local Taxes Collectibles and Actual Collections By Item (2019-2023)', fontsize=16)
plt.xlabel('Barangay', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + 2*bar_width, barangays, rotation=90)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
