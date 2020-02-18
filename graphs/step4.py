# This is a graph for 2 times x^3 plus 3 when x is ranging from -1 to 14
import math
import matplotlib.pyplot as pyplot
x = [i for i in range(-1,14)]
y = [2 * (i**3) + 3 for i in x]

    pyplot.plot(x, y)
    pyplot.xlabel('x')
    pyplot.ylabel('$y = 2x^2 + 3$')
    pyplot.show()

