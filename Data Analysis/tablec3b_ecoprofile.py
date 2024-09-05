import matplotlib.pyplot as plt
import numpy as np

years = ["2019", "2020", "2021", "2022", "2023"]

tax_revenues = [124.76, 113.22, 133.45, 105.58, 114.91]
real_property_tax = [78.01, 72.21, 70.65, 86.69, 192.96]
tax_on_business = [158.38, 149.41, 198.65, 124.12, 98.37]
other_taxes = [167.93, 141.36, 153.82, 87.53, 54.32]
non_tax_revenues = [104.80, 119.70, 125.93, 98.41, 81.63]


bar_width = 0.15
index = np.arange(len(years))


plt.figure(figsize=(14, 8))
plt.bar(index, tax_revenues, bar_width, label='Total Tax Revenues')
plt.bar(index + bar_width, real_property_tax, bar_width, label='Real Property Tax')
plt.bar(index + 2*bar_width, tax_on_business, bar_width, label='Tax on Business')
plt.bar(index + 3*bar_width, other_taxes, bar_width, label='Other Taxes')
plt.bar(index + 4*bar_width, non_tax_revenues, bar_width, label='Non-Tax Revenues')

plt.title('Collection Efficiency (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Collection Efficiency (%)', fontsize=14)
plt.xticks(index + 2*bar_width, years)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
