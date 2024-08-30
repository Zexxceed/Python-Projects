import matplotlib.pyplot as plt

# Data for the plot
years = ["2019", "2020", "2021", "2022", "2023"]

# Annual Growth Rates
tax_revenues = [9.83, -7.28, 24.57, -6.73, 36.42]
real_property_tax = [-10.79, -2.75, 2.73, 6.23, 126.91]
tax_on_business = [18.99, -5.66, 39.60, -2.22, 5.64]
other_taxes = [23.31, -16.03, 18.63, -34.67, -8.58]
non_tax_revenues = [20.28, 19.13, 11.04, -8.95, 6.73]

# Create a plot
plt.figure(figsize=(14, 8))

# Plotting each category
plt.plot(years, tax_revenues, marker='o', label='Total Tax Revenues')
plt.plot(years, real_property_tax, marker='o', label='Real Property Tax')
plt.plot(years, tax_on_business, marker='o', label='Tax on Business')
plt.plot(years, other_taxes, marker='o', label='Other Taxes')
plt.plot(years, non_tax_revenues, marker='o', label='Non-Tax Revenues')

# Adding titles and labels
plt.title('Annual Growth Rate of Revenues and Receipts By Source (2019-2023)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Growth Rate (%)', fontsize=14)
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
