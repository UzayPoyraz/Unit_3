1) 
# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())  # distance to enemy 2

    # Write an action using print

    # Enter the code here
    
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
        
2)
The Descent:
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    shoot = 0
    height = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.  
        if mountain_h>height:
            shoot=i
            height=mountain_h
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # The index of the mountain to fire on.
    print(shoot)
