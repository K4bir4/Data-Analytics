##2. Create a NumPy array of shape (4, 4) with values from 1 to 16. Replace the diagonal elements with 0.
# Create a NumPy array of shape (4, 4) with values from 1 to 16
array = np.arange(1, 17).reshape((4, 4))
print("Original array:")
print(array)

# Replace the diagonal elements with 0
np.fill_diagonal(array, 0)
print("Modified array:")
print(array)
