import turtle

color_line = turtle.Turtle()

color_line.pencolor("blue")

for i in range(50):
    color_line.forward(50)
    color_line.left(123)

    color_line.pencolor("red")
    for i in range(50):
        color_line.forward(100)
        color_line.left(123)

    color_line.pencolor("green")
    for i in range(50):
        color_line.forward(50)
        color_line.left(123)

    color_line.pencolor("yellow")
    for i in range(100):
        color_line.forward(100)
        color_line.right(123)


