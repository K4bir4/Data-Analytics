array = np.random.randint(1,21, size = (5,5))
print("original array : \n", array)

##flattem the array
flatarray = array.flatten()
print("flattened array :\n", flatarray)

#reshape array back to 
reshapearray = flatarray.reshape((5,5))
print("reshaped array :\n",reshapearray)
