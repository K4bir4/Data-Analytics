##create numpy array of shape 55
array = np.random.randint(1,21, size=(5,5))
print(f"Original array :\n{array}\n")

#compute the statistical values
mean=np.mean(array)
median = np.median(array)
std_dev=np.std(array)
variance=np.var(array)

print("Mean :", mean)
print("Median :", median)
print("std dev :",std_dev)
print("variance :", variance)
