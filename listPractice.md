Practice 1 :
num = input().split()
for i in range(0, len(num), 2):
  print(num[i])
Practice 2: (I'm having problems with this one(ask later))

num = input().split()
for i in range(0, len(num) , 2):
for element in num:
    print (element)
    
Practice 3:
num = input().split()
for i in range (1, len(num)):
    if num[i] > num[i-1]:
        print(num[i])
Practice 4:
I really didn't understand the question! I will ask this one as well

Practice 5:
num = input().split()
sum = 0
for i in range(len(num)):
    num[i] = int(num[i])
for i in range (1, len(num)-1):
    if num[i-1] < num[i] > num[i+1]:
        sum += 1
print(sum)
