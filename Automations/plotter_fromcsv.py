import pandas as pd

# Load the CSV file
df = pd.read_csv('C:/Users/Zexxceed/Desktop/Python Projects/total_population_dupaxdelsur.csv')

# Example: Plot total population over time using Matplotlib
import matplotlib.pyplot as plt

plt.plot(df['Year'], df['Population'], marker='o')
plt.title('Population Growth of Dupaxx Del Sur')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
