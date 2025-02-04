!pip install matplotlib
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]

##create a line plot
plt.plot(x,y)
plt.xlabel('X axis')
plt.ylabel('Y Axis')
plt.title("Basic Line Plot")
plt.show()
