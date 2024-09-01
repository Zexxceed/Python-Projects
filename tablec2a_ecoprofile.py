import matplotlib.pyplot as plt
import numpy as np

years = ["2019", "2020", "2021", "2022", "2023"]

real_property_tax = [1243501.39, 1209868.15, 1223360.58, 1322653.87, 2999854.76]
tax_on_business = [994604.85, 938311.36, 1309915.70, 1280868.63, 1353119.69]
other_taxes = [470204.42, 394812.26, 468381.44, 306005.91, 279764.81]
regulatory_fees = [553229.31, 509708.62, 698198.64, 809125.73, 741575.70]
service_user_charges = [2889984.50, 3725483.35, 4162063.11, 3579993.00, 3924694.45]
other_receipts = [455662.32, 408193.39, 295570.36, 305258.90, 344190.51]
special_education_fund = [689621.01, 671194.48, 669974.35, 734809.26, 1665951.87]


bar_width = 0.1
index = np.arange(len(years))


plt.figure(figsize=(14, 8))
plt.bar(index, real_property_tax, bar_width, label='Real Property Tax')
plt.bar(index + bar_width, tax_on_business, bar_width, label='Tax on Business')
plt.bar(index + 2*bar_width, other_taxes, bar_width, label='Other Taxes')
plt.bar(index + 3*bar_width, regulatory_fees, bar_width, label='Regulatory Fees')
plt.bar(index + 4*bar_width, service_user_charges, bar_width, label='Service/User Charges')
plt.bar(index + 5*bar_width, other_receipts, bar_width, label='Other Receipts')
plt.bar(index + 6*bar_width, special_education_fund, bar_width, label='Special Education Fund')

plt.title('Local Revenues and Receipts By Source (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Amount (in PHP)', fontsize=14)
plt.xticks(index + 2*bar_width, years)
plt.legend()
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.show()
