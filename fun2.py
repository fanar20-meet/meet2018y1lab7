
'''
import turtle
turtle.goto(0,0)

def up():
    print("You pressed the up key.")
    
turtle.onkey(up, "Up") 
turtle.listen()
'''

import turtle
    
direction = None
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
   
def up():
    global direction
    direction = UP
    print("You pressed the up key.")

def right():
    global direction
    direction = RIGHT
    print("you pressed the right key")
    
def down():
    global direction
    direction = DOWN
    print('you pressed the down key')
    
def left():
    global direction
    direction = LEFT
    print('you pressed the left key')

turtle.onkey(up, "Up")
turtle.onkey(down, "Down") 
turtle.onkey(right, "Right")
turtle.onkey(left, "Left")
turtle.listen()


def on_move():
    y_change = 100
    x_change = 200
    x,y = turtle.position()
    if direction == UP:
         turtle.goto(x,y+y_change)
    elif direction == DOWN :
        turtle.goto(x,y-y_change)
    elif direction == LEFT :
        turtle.goto(x-x_change,y)
    elif direction == RIGHT :
        turtlr.goto(x=x_change,y)

turtle.mainloop()

    

