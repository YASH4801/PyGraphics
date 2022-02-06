import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.pencolor('Red')
t.speed(100)
n = 200
h = 0
for j in range(150):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h+=1/n
    t.color(c)
    t.circle(190-j, 90)
    t.lt(90)
    t.circle(190-j, 90)
    t.lt(18)
s.exitonclick()