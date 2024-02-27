import turtle
import colorsys
s = turtle.Turtle()
m = turtle.Screen()
m.bgcolor("black")
s.speed(0)
s.pensize(15)
n = 50
h = 9
while True:
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1 / n
    s.color(c)
    s.forward(2)
    s.left(1)
turtle.done()