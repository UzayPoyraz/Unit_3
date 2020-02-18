import random
import matplotlib.pyplot as pyplot
from numpy import mean
sum = 0
for i in range (1000):
    x = i
    y = random.randrange(0, 100)
    sum += y
avg = sum/1000
print("average is", avg)

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()

