import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv('covid_data.csv')  # Replace with your file path

# Task 1: Filter Data by Country
country_name = 'India'  # Specify the country for analysis
country_data = data[data['Country'] == country_name]  # Filter data for the specified country

# Task 2: Group by Date
# Ensure the 'Date' column is in datetime format
country_data['Date'] = pd.to_datetime(country_data['Date'])

# Group by date and aggregate the data
daily_data = country_data.groupby('Date').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
}).reset_index()

# Calculate daily changes
daily_data['Daily Confirmed'] = daily_data['Confirmed'].diff().fillna(0)
daily_data['Daily Deaths'] = daily_data['Deaths'].diff().fillna(0)
daily_data['Daily Recovered'] = daily_data['Recovered'].diff().fillna(0)

# Task 3: Visualize Trends
plt.figure(figsize=(12, 6))
plt.plot(daily_data['Date'], daily_data['Daily Confirmed'], label='Daily Confirmed', color='blue', linewidth=2)
plt.plot(daily_data['Date'], daily_data['Daily Deaths'], label='Daily Deaths', color='red', linewidth=2)
plt.plot(daily_data['Date'], daily_data['Daily Recovered'], label='Daily Recovered', color='green', linewidth=2)

# Adding titles and labels
plt.title(f'COVID-19 Trend Analysis in {country_name}', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Cases', fontsize=12)
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()

# Show the plot
plt.show()
