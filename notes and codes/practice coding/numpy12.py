array1= np.random.randint(1,11,size=(2,3))
array2= np.random.randint(1,11,size=(3,2))
print("array 1 :\n",array1)
print("array 2 :\n",array2)

##perfrom matrix multiplicaiton
result = np.dot(array,array2)
print("result = \n",result)
