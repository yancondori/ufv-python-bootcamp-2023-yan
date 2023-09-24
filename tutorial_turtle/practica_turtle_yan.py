import turtle
import random2

# opening turtle window
s = turtle.getscreen()

#initialize the variable t
t = turtle.Turtle()

#Moving the Turtle Forward, Backward, Left, Right: . .forward() or .fd() method etc..
# t.right(90) # each represents a movement 
# t.forward(100)
# t.left(90)
# t.backward(100)

#Moving the Turtle across the 4 cartesian quadrants, initialize first s and t variables
#t.goto(100,100)

#quadrant point (0,0) = home
t.home()

#drawing a circle shape
t.circle(60)

#drawing a dot
t.dot(20)

#setting window color
turtle.bgcolor("blue")

#changing the title screen
turtle.title("My Turtle Yan")

#Changing the Turtle Size
t.shapesize(1,5,10)
t.shapesize(10,5,1)
t.shapesize(1,10,5)
t.shapesize(10,1,5)

#Changing Pen Size
t.pensize(5)
t.forward(100)

#setting shape color of fill it
t.fillcolor("red")
t.pencolor("green")

#1.TO SUMUP, run 2 times:
t = turtle.Turtle()
t.shapesize(3,3,3)
t.fillcolor("red")
t.pencolor("green")

#------------------------------
#------------------------------
#filling a figure shape
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

# changing the way the turtle looks
t.shape("turtle") # to get turtle shape
t.shape("arrow") # to get an arrow..
t.shape("circle")

# changing the speed pen
t.speed(1)
t.forward(100)

t.speed(10)
t.forward(100)

#2.To SUMUP Customizing in One Line
t.pen(pencolor="purple", fillcolor="orange", pensize=10, speed=9)
t.begin_fill()
t.circle(90)
t.end_fill()


#------------------------------
#------------------------------
# Picking the Pen Up and Down
t = turtle.Turtle()
t.fd(100)
t.rt(90)
t.penup() # NO DRAW THE LINE, ONLY ICON
t.fd(100)
t.rt(90)
t.pendown() # TO DRAW THE LINE
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

# Undone previous action
t.undo() 

# clearing ie drawned lines 
t.clear()

# initialize from the beginning  
t.reset()

# stamping, or pasting
t.stamp()

t.fd(100)
t.stamp()

t.fd(100)

# clearing stamp
t.clearstamp(8)

#------------------------------
#------------------------------
# Cloning previous figure
t.reset() # VERY USEFUL 
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)

#-- LOOPS AND CONDITIONALS----------------------------
#------------------------------
# Looping previous Picking the Pen Up and Down
t = turtle.Turtle()
t.clear()
# Range works from 0 to n and  It will terminate the program before i reaches n
for i in range(3):
    t.fd(100)
    t.rt(90)

# The while loop is used to perform a certain task while a condition is still satisfied.
t.clear()    
n=10
while n <= 40:
    t.circle(n)
    n = n+10

# conditional for drawing a circle.
t.clear()    

u = input("Would you like me to draw a shape? Type yes or no: ")

if u == "yes":
    t.circle(50)
elif u == "no":
    print("Okay")
else:
    print("Invalid Reply")

