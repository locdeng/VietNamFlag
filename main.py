import turtle
from turtle import*

screen = turtle.Screen()
flag = turtle.Turtle()

# Setting up the Turtle

speed(0)  # sets up the drawing speed of the turtle to the fastest
flag.penup()  # lifts the turtle's pen, so it doesn't draw while moving
flag.goto(-250, 150)  # move the turtle to the initial position where the flag drawing starts
flag.pendown()  # lowers the turtle's pen, sp it can start drawing

flag.color("red")
flag.begin_fill()
flag.forward(500)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(500)
flag.right(90)
flag.end_fill()



# Draw the yellow star
flag.penup()
flag.goto(-5, 65)
flag.setheading(-72)  # Set the turtle's heading (rotation angle) to -72 degrees
flag.pendown()
flag.pendown()
flag.color("yellow")
flag.begin_fill()
for _ in range(5):
    flag.forward(120)
    flag.right(144)
flag.end_fill()

# Hide the turtle and display the flag
flag.hideturtle()
turtle.done()
