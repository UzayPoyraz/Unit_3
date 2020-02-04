#This program will count the amount of zeros entered in a program
a=int(input("Enter a number:"))
amount=0
for i in range(1,a+1):
  x= int(input("Enter a number:"))
  if x==0:
    amount=amount+1
print"The amount of 0 is: ",amount
