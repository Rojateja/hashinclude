import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv('covid_data.csv')  

# Filter Data by Country (e.g., India)
country_name = 'India'
country_data = data[data['Country'] == country_name]

# Ensure the 'Date' column is in datetime format
country_data['Date'] = pd.to_datetime(country_data['Date'])

# Task 1: Resample Data to Weekly Frequency
country_data.set_index('Date', inplace=True)  # Set the date as index
weekly_data = country_data.resample('W').sum()  # Aggregate weekly

# Task 2: Calculate 7-day Rolling Average
weekly_data['7-day Rolling Avg'] = weekly_data['Confirmed'].rolling(window=7).mean()

# Deliverables: A weekly aggregated dataset
print(weekly_data[['Confirmed', '7-day Rolling Avg']])

# Task 3: Visualize the Rolling Average
plt.figure(figsize=(12, 6))
plt.plot(weekly_data.index, weekly_data['Confirmed'], label='Weekly Confirmed Cases', color='blue', alpha=0.5)
plt.plot(weekly_data.index, weekly_data['7-day Rolling Avg'], label='7-Day Rolling Average', color='orange', linewidth=2)

# Adding titles and labels
plt.title(f'Weekly COVID-19 Confirmed Cases and 7-Day Rolling Average in {country_name}', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Cases', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()

# Show the plot
plt.show()
