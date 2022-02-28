from turtle import *
import shapes
t = Turtle()
s = Screen()
s.bgcolor('black')
t.color('green')
# shapes.square(-150, 0, t, 100)
color('green')
begin_fill()
shapes.ractangle(-200, 300, t, 200, 400)
end_fill()
done()