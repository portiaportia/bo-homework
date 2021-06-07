# Lab 7: Color Arrays
# Author: Bo Rogers

import turtle
import random

t = turtle.Pen()
t.speed(0)
t.width(7)
t.penup()

shapes = ("truck", "car")
numShapes = int(input("How many shapes do you want?"))
colors = ("blue","green","red")

#Display Shapes
for i in range(numShapes):
    shapeType = random.randint(0,1)

    if(shapeType == 0):
        #draw truck
        for i in range(30):
            x = random.randrange(-int(turtle.window_width()/2),int(turtle.window_width()/2))
            y = random.randrange(-int(turtle.window_height()/2),int(turtle.window_height()/2))
            t.setpos(x,y)
            t.pendown()
            t.speed(0)
            t.fillcolor("random.color")
            t.left(180)
            t.forward(140)
            t.left(90)
            t.forward(30)
            t.left(90)
            t.forward(200)
            t.left(90)
            t.forward(40)
            t.left(90)
            t.forward(25)
            t.right(90)
            t.forward(25)
            t.left(90)
            t.forward(35)
            t.left(90)
            t.forward(35)
            t.end_fill()
            t.penup()
    elif shapeType == 1:
        #draw car
        for i in range(30):
            x = random.randrange(-int(turtle.window_width()/2),int(turtle.window_width()/2))
            y = random.randrange(-int(turtle.window_height()/2),int(turtle.window_height()/2))
            t.pendown()
            t.fillcolor(random.choice(colors))
            t.speed(0)
            t.left(90)
            t.forward(25)
            t.left(90)
            t.forward(150)
            t.left(45)
            t.forward(50)
            t.left(45)
            t.forward(35)
            t.left(90)
            t.forward(225)
            t.left(90)
            t.forward(40)
            t.left(90)
            t.forward(40)
            t.end_fill()
            t.penup()