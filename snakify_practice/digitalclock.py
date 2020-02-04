#The input entered to this program is the amount of minutes it has passed since midnight, this program will tell you the time passed after midnight in 24h time
a = int(input("Enter how many minutes it has passed since midnight: "))
hour = a//60
minute = a % 60
print "The time is",hour, minute
