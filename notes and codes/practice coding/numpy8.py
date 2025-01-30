##array of shape (3,3) with values 1 to 9
array = np.arange(1,10).reshape((3,3))
print("original array : \n",array)

#lets normalize
mean = np.mean(array)
std_dev = np.std(array)
normalized_array = (array - mean)/ std_dev

print("normalized arraayy:\n",normalized_array)
