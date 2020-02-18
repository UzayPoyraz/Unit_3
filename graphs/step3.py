import math
import matplotlib.pyplot as pyplot
x = [i for i in range (-10, 10)]
y = (14 * math.sin(0.5 * x))
    pyplot.plot(x, y)
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.show()
