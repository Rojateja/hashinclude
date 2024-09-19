import pandas as pd

# Load the COVID-19 data
covid_data = pd.read_csv('covid_data.csv')  

# Load the population data
population_data = pd.read_csv('population_data.csv')  

# Task 1: Merge Population Data
# Assuming the population data has columns 'Country' and 'Population'
merged_data = pd.merge(covid_data, population_data, on='Country', how='left')

# Task 2: Calculate Cases per Capita
# Assuming 'Confirmed Cases' is the column for confirmed COVID-19 cases
merged_data['Cases per Capita'] = merged_data['Confirmed'] / merged_data['Population']

# Task 3: Rank Countries by Confirmed Cases per Capita
ranked_data = merged_data[['Country', 'Confirmed', 'Population', 'Cases per Capita']]
ranked_data = ranked_data.sort_values(by='Cases per Capita', ascending=False)

# Deliverables: A merged dataset and a list of the top 10 countries
print("Merged Dataset:")
print(merged_data[['Country', 'Confirmed', 'Population', 'Cases per Capita']])

top_10_countries = ranked_data.head(10)
print("\nTop 10 Countries by Confirmed Cases per Capita:")
print(top_10_countries)
