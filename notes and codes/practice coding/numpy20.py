import numpy.ma as ma

#create a mask array of shape 4 4 wiht random integers
array = np.random.randint(1,21, size = (4,4))
masked_array = ma.masked_greater(array,10)
print("org array : \n",array)
print("msked array : \n",masked_array)

#commpute the sum of unmaksed elements
sum_unmasked=masked_array.sum()
print("sum of unmmasked ele:",sum_unmasked)
