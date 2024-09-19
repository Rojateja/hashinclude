import pandas as pd
# Load the dataset
df = pd.read_csv('covid_data.csv')

# Display the first few rows
print(df.head())

# Check data types and missing values
print(df.info())

# Display basic statistics
print(df.describe())
