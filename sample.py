import turtle
san = turtle.Turtle()

san.speed(200)

san.pencolor("blue")

for i in range(110):
  san.left(123)
  san.forward(75)


san.left(120)
san.forward(50)
san.right(110)
san.forward(25)
san.left(90)
san.pencolor("green")
san.forward(290)
san.backward(600)

for i in range(250):
  san.right(90)
  san.forward(.30)
  san.left(90)
  san.forward(600)
  san.backward(600)


san.pencolor("black")

san.left(90)
san.forward(160)
san.right(90)
san.forward(600)
san.backward(600)

for i in range(250):
  san.pencolor("orange")
  san.left(90)
  san.forward(.30)
  san.right(90)
  san.forward(600)
  san.backward(600)


san.pencolor("black")
san.forward(600)
san.right(90)
san.forward(250)