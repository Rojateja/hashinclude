import pandas as pd
import matplotlib.pyplot as plt

# Load the data from a CSV file
data = pd.read_csv('covid_data.csv')  

# Task 1: Filter Data by Country
country_data = data[data['Country'] == 'India']  # Replace 'India' with the desired country

# Task 2: Group by Date
# Assuming the data has 'Date', 'Confirmed Cases', 'Deaths', and 'Recovered Cases' columns
country_data['Date'] = pd.to_datetime(country_data['Date'])  # Convert to datetime
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
plt.plot(daily_data['Date'], daily_data['Daily Confirmed'], label='Daily Confirmed', color='blue')
plt.plot(daily_data['Date'], daily_data['Daily Deaths'], label='Daily Deaths', color='red')
plt.plot(daily_data['Date'], daily_data['Daily Recovered'], label='Daily Recovered', color='green')

plt.title('COVID-19 Trend Analysis in India')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
