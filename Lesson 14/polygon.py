#draw polygon with turtle library
import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
polygon.speed(1)
num_sides = 6
side_len = 70
angle = 360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_len)
    polygon.right(angle)
    


turtle.done()