#This program will show if the rock can go from one cell to the other in 1 move
a = int(input("The location of first cell (horizontal) {1-8}: "))
b = int(input("The location of first cell (vertical) {1-8}: "))
c = int(input("The location of the second cell (horizontal): " ))
d = int(input("The location of the second cell (vertical): " ))

if a == c or b == d:
  print "Yes"
else:
  print "No"
