# BAR PLOT
# Problem Statement: Comparing categorical data using a bar chart.
# Question: Which category has the highest value in the given dataset?

# Define categories and their corresponding values
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create bar chart
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart")
plt.show()
