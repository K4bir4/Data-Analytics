##2. Create a NumPy array of shape (5, 5) with random integers. Extract the elements on the border.
# Create a NumPy array of shape (5, 5) with random integers
array = np.random.randint(1, 21, size=(5, 5))
print("Original array:")
print(array)

# Extract the elements on the border
border_elements = np.concatenate((array[0, :], array[-1, :], array[1:-1, 0], array[1:-1, -1]))
print("Border elements:")
print(border_elements)
