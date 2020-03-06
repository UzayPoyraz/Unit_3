1) 
```
#game loop
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
 
```
        
### 2)
### The Descent:
`` 
import sys
import math

#The while loop represents the game.
#Each iteration represents a turn of the game
#where you are given inputs (the heights of the mountains)
#and where you have to print an output (the index of the mountain to fire on)
#The inputs you are given are automatically updated according to your last actions.


#game loop
while True:
    shoot = 0
    height = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.  
        if mountain_h>height:
            shoot=i
            height=mountain_h
    #Write an action using print
    #To debug: print("Debug messages...", file=sys.stderr)

    #The index of the mountain to fire on.
    print(shoot)``
3)Thor's power:
```import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    directionX=""
    directionY=""
    if light_y>light_y:
        directionY+="N"
        initial_ty-=1
    elif initial_ty<light_y:
        directionY+="S"
        initial_ty+=1
    if initial_tx>light_x:
        directionX+="W"
        initial_tx+=1
    elif initial_tx<light_x:
        directionX+="E"
        initial_tx-=1
    
    print(directionY+directionX)    
   

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    ```
