##1. Create a NumPy array of shape (6, 6) with values from 1 to 36. Extract the sub-array consisting of the 3rd to 5th rows and 2nd to 4th columns.
# Create a NumPy array of shape (6, 6) with values from 1 to 36
array = np.arange(1, 37).reshape((6, 6))
print("Original array:")
print(array)

# Extract the sub-array
sub_array = array[2:5, 1:4]
print("Sub-array:")
print(sub_array)
