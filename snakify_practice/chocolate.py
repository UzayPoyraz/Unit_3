I found this solution online, now I understand where I was struggling
#This program will show you if the chocolate of portions nxm can have k equal squares
n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
    print('YES')
else:
    print('NO')
