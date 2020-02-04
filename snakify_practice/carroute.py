#This program will get how many kilometers a car can travel a day and shows how many days it takes to travel an inputted distance
a = int(input("Enter how many kilometers the car can travel: "))
b = int(input("Enter how many kilometers you want to travel with the car: "))
if (a*2>b):
  print "The amount of days it will take you is: 1",
else:
  print "The amount of days it will take you is: ", b//a
