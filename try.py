import turtle

sun = turtle.Turtle()

sun.speed(3)

sun.pencolor("red")

for i in range(7):
    sun.forward(85)
    sun.right(360.0 / 6)

sun.pencolor("brown")

for i in range(6):
    sun.forward(853.3)
    sun.left(360.0 / 6)


sun.pencolor("blue")

sun.right(120)

for i in range(7):
  sun.forward(85)
  sun.right(360.0 / 6)


sun.pencolor("green")

sun.right(120)
sun.forward(85)
sun.right(360.0 / 6)
sun.forward(85)
sun.right(360.0 / 6)
sun.forward(85)
sun.left(360.0 / 6)
sun.forward(85)
sun.left(60)
sun.forward(85)
sun.left(360.0 / 6)
sun.forward(85)
sun.left(360.0 / 6)
sun.forward(85)
sun.left(360.0 / 6)
sun.forward(85)

sun.pencolor("orange")

sun.right(180)
sun.forward(85)


turtle.done