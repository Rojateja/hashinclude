import pandas as pd

# Load the COVID-19 data
data = pd.read_csv('covid_data.csv')  # Replace with your COVID-19 data file path

# Task 1: Summarize Key Metrics
# Group data by country and calculate total confirmed cases, deaths, recoveries
summary_data = data.groupby('Country').agg({
    'Confirmed': 'sum',
    'Deaths': 'sum',
    'Recovered': 'sum'
}).reset_index()

# Calculate fatality rate
summary_data['Fatality Rate'] = (summary_data['Deaths'] / summary_data['Confirmed']) * 100

# Deliverables: A summary dataset
print("Summary of Key Metrics:")
print(summary_data)

# Task 2: Export to CSV
# Define the filename with your name and hash
my_name = 'Roja'  # Replace with your actual name
summary_data.to_csv(f'{my_name}_hashInclude.csv', index=False)

print(f"\nSummary report exported to {my_name}_hashInclude.csv")
