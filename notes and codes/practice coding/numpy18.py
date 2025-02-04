# create structured array with fields
data_type=[('name','U10'),('age','i4'),('weight','f4')]
data=np.array([('alice',25,55.5),('Bob',30,85.3),('Charlie',20,65.2)],dtype =data_type)
print("orignal array :")
print(data)

#sort the arraey by age
sorted_data = np.sort(data,order='age')
print("sorted_data : ")
print(sorted_data)
