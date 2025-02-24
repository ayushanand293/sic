# Generating 23 equally spaced values between 0 and 100

# Explanation: Using np.linspace() to generate specified number of values in a range

import numpy as np

values = np.linspace(0, 100, 23)
print("Generated values:", values)
print("Total count:", len(values))
