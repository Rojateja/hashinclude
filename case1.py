import pandas as pd

# Load the data from a CSV file
data = pd.read_csv('covid_data.csv')

# Group data by country
grouped_data =   data.groupby('Country').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
}).reset_index()

# Calculate Fatality Rate
grouped_data['Fatality Rate'] = (grouped_data['Deaths'] / grouped_data['Confirmed']) 

# Sort by Confirmed Cases and get the top 10
top_countries = grouped_data.sort_values(by='Confirmed', ascending=False).head(10)

# Display the result
print(top_countries)


