import pandas as pd

df = pd.read_csv('C:/Users/Zexxceed/Desktop/Work/Ecological Profile/CSV Files (EP)/total_population_dupaxdelsur.csv')

import matplotlib.pyplot as plt

plt.plot(df['Year'], df['Population'], marker='o')
plt.title('Population Growth of Dupax Del Sur')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
