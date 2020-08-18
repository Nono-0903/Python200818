import turtle
import time

a = turtle.Turtle()
b = turtle.Turtle()

screen = turtle.Screen()
screen.title("Sky")
screen.bgcolor("lightblue")


a.pensize(5)
a.color('white')
a.shape('turtle')

b.pensize(5)
b.color('white')
b.shape('turtle')

for i in range(720):
    a.forward(1)
    a.left(0.5)
    b.forward(1)
    b.right(0.5)

turtle.done()