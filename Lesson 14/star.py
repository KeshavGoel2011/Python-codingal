# Star with turtle library
import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,400)
star = turtle.Turtle()


star.forward(100)
star.left(120)

star.forward(100)
star.left(120)

star.forward(100)

star.penup()
star.right(150)
star.forward(50)
star.pendown()

star.right(90)
star.forward(100)

star.right(120)
star.forward(100)

star.right(120)
star.forward(100)

turtle.done()