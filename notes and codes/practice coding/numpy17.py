#create numpy array
array= np.random.randint(1,21, size=(4,4))
print("original array : \n",array)

#use boolean indexing to set all elements greater than 10 to 10
array[array>10]= 10
print("modded array :\n",array)
