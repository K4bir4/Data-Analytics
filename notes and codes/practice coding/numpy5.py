#create 2 arrays with numpy of size 3,4 filled with rand int
array1= np.random.randint(1,21, size= (3,4))
array2= np.random.randint(1,21,size= (3,4))
print("array1 :")
print(array1)
print("array2 :")
print(array2)

#performing element wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1/ array2

print(f"{addition}\n")
print(f"{subtraction}\n")
print(f"{multiplication}\n")
print(f"{division}\n")
