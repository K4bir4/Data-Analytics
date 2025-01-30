#create a numpy array of shape 4 4 with vlaue 1 to 16
array = np.arange(1,17).reshape((4,4))
print("original array :")
print(array)

#compute the row wise and column wise sum
row_sum = np.sum(array, axis =1)
column_sum = np.sum(array, axis=0)

print(f"row wise sum : {row_sum}\n")
print(f"column wise sum : {column_sum}\n")
