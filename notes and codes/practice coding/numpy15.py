##numpy 15
array= np.random.randint(1,21, size=(5,5))
print("original array : \n",array)

#using fancy indexing
corners = array [[0,0,-1,-1],[0,-1,0,-1]]
print("corner elements :", corners)
