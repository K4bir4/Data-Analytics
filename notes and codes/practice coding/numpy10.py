array = np.random.randint(1,11, size=(4,4))
column_array = np.random.randint(1,11,size=(4,))
print("original array :\n ", array)
print("column array :\n",column_array)

##subtract tht 1d array from each column of 2d aray
result = array - column_array[:,np.newaxis]
print("resulting array : \n",result) 
