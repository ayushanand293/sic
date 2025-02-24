# Filtering rows where Salary > 50000

# Explanation: Using boolean indexing to filter rows based on Salary column
import pandas as pd

df = pd.read_csv(r'C:\Learning\Python\sic\day7\datascience_salaries.csv')  # Reads the CSV file
high_salary = df[df['salary'] > 50000]  # Filters rows based on Salary
print(high_salary)
