import numpy as np
from scipy import stats

# Create a NumPy array
array = np.array([1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12])

# Calculate mean, median, and mode
mean = np.mean(array)
median = np.median(array)
mode_result = stats.mode(array)

# Accessing the mode and count directly
mode_value = mode_result.mode[0]
mode_count = mode_result.count[0]

# Print the results
print(f'Mean = {mean}')
print(f'Median = {median}')
print(f'Mode = {mode_value}, Count = {mode_count}')

# Optional: Check the version of scipy
import scipy
print(f'Scipy version: {scipy.__version__}')