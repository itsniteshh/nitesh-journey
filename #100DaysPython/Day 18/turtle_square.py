from turtle import Turtle, Screen

def turn_right():
    nit.forward(100)
    nit.right(90)
    nit.forward(100)
    nit.right(90)
    nit.forward(100)
    nit.right(90)
    nit.forward(100)
    

nit = Turtle()
nit.shape("turtle")
nit.color("red")
#turn_right()


screen_time = Screen()
screen_time.exitonclick()