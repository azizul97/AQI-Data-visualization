import matplotlib.pyplot as plt

# Data for air pollution index (PM2.5 concentration in µg/m³) in Bangladesh
years = [2019, 2020, 2021, 2022, 2023, 2024]
pm25_values = [83.3, 77.5, 80.1, 85.6, 90.2, 95.4]  # Estimated values based on trend

plt.figure(figsize=(10, 5))
plt.bar(years, pm25_values, color=['red', 'orange', 'orange', 'red', 'darkred', 'darkred'])

plt.xlabel("Year")
plt.ylabel("PM2.5 Concentration (µg/m³)")
plt.title("Air Pollution Index (PM2.5) in Bangladesh (2019-2024)")
plt.xticks(years)
plt.ylim(0, 100)  # Setting limit for better visualization

plt.show()

