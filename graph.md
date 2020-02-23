# Graph an exponential function: f(x) = (x+1)^2 - 1, with x from -2, to 2 with 1000 points:
### (There are some problems with the graph) 
### (The graph shows very big numbers, I do not know how to prevent that)
import matplotlib.pyplot as pyplot
x = []
y = []
min = -2
for i in range (1000):
    x.append(min * (i+1))
    y.append(((x[i]+1)**2)-1)
pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
