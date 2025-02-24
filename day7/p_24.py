# VIOLIN PLOT
# Problem Statement: Comparing multiple distributions using a violin plot.
# Question: How does the density of data differ across categories?

# Create violin plot
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.randn(100) for _ in range(4)]

plt.violinplot(data)
plt.xlabel("Category")
plt.ylabel("Values")
plt.title("Violin Plot")
plt.show()
