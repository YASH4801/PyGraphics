import turtle as tu
k = tu.Turtle()
def square(x, y, k, side=0):
    k.penup()
    k.goto(x,y)
    k.pendown()
    for i in range(4):
        k.forward(side)
        k.right(90)
    k.hideturtle()
    
def ractangle(x, y, k, height, width):
    k.penup()
    k.goto(x,y)
    k.pendown()
    for i in range(2):
        k.forward(width)
        k.right(90)
        k.forward(height)
        k.right(90)
    k.hideturtle()