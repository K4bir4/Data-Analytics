array = np.random.randint(1,11, size = (3,3))
row_array = np.random.randint(1,11, size= (3,))
print("original array :", array)
print("1d array :", row_array)

#add the 1 d array to the array
result = array + row_array
print("resutling array :",result)
