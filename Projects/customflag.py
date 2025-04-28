import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")

height = 100

# move to stripe 4
t.goto(-250, 0)

# stripe 4
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()



# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

turtle.exitonclick()
