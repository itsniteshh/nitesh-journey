from turtle import Turtle, Screen

# Create a turtle object
nit = Turtle()

# Set the turtle's pen to be dashed
for i in range(15):
    nit.forward(10)
    nit.penup()
    nit.forward(10)
    nit.pendown()

# Move the turtle forward to draw a dashed line


# Exit turtle
my_screen = Screen()
my_screen.exitonclick()