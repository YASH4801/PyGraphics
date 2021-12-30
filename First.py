import turtle as x
x.speed("fastest")
x.bgcolor("black")
x.pensize(2)

def tree(blen, x):
    if blen > 4:
        x.forward(blen)
        x.right(20)
        tree(blen-15, x)
        x.left(40)
        tree(blen-15, x)
        x.right(20)
        x.backward(blen)

def main():
    mywin = x.Screen()
    x.left(90)
    x.up()
    x.backward(200)
    x.down()
    x.color("green")
    tree(105, x)
    mywin.exitonclick()

main()
    
    