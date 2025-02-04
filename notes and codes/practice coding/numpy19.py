#create a strcutured aray with firld x and  y
data_type = [('x','i4'),('y','i4')]
data = np.array([(1,2),(3,4),(5,6)], dtype= data_type)
print("original array :")
print(data) 

#compute the euclidean distance betwn each pair of points
distances = np.sqrt((data['x'][:, np.newaxis]- data['x'])**2 +(data['y'][:, np.newaxis]- data['y'])**2 )
print("euclidean distances :")
print(distances)
