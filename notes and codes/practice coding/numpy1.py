##practice solutions of numpy
##. Create a NumPy array of shape (5, 5) filled with random integers between 1 and 20. Replace all the elements in the third column with 1.
import numpy as np

# Create a NumPy array of shape (5, 5) filled with random integers
array = np.random.randint(1, 21, size=(5, 5))
print("Original array:")
print(array)

# Replace all the elements in the third column with 1
array[:, 2] = 1
print("Modified array:")
print(array)
