from turtle import *
speed(1000)
color('cyan')
bgcolor('black')
b = 200
while b > -100:
    left(b)
    forward(b*3)
    b-=1
exitonclick()