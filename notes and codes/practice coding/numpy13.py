array= np.arange(1,10).reshape((3,3))
print("original array : \n", array)

#reshape the array to 1 9
res_arr_1 = array.reshape((1,9))
print("reshaped array1 : \n",res_arr_1)

##reshape the arry to 9 1
res_arr_2= array.reshape((9,1))
print("reshaped array2 : \n",res_arr_2)
