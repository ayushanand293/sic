# Reading a CSV file and checking for missing values

# Explanation: Using pd.read_csv() to load data and checking for missing values using isnull()

import pandas as pd

df = pd.read_csv(r'C:\Learning\Python\sic\day7\bike_sales_india.csv')  # Reads the CSV file
df.head()  # Displays the first 5 rows
print(df.isnull().sum())  # Counts missing values in each column

df_sorted = df.sort_values(by='salary', ascending=False)
print(df_sorted)

