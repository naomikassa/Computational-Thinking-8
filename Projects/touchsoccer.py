# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle
import math
import time
import random


def set_background(image_filename):
    screen = turtle.Screen()
    try:
        screen.bgpic(
            f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
    except:
        screen.bgpic(
            f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    return sprite


def get_distance(s1, s2):
    dx = s1.xcor() - s2.xcor()
    dy = s1.ycor() - s2.ycor()
    return math.sqrt(dx*dx + dy*dy)


window = turtle.Screen()
window.tracer(0)
# Section 2: Setup
s1 = create_sprite("s1", -200, -200)

s2 = create_sprite("s2", 200, -200)

# TODO - set your background
set_background("soccerfield")
# TODO - set the starting value for your variable

# Section 3: Controls
# TODO - define your controls


def move_for():
    s1.setheading(90)
    s1.forward(10)


def move_down():
    s1.setheading(270)
    s1.forward(10)


def move_left():
    s1.setheading(180)
    s1.forward(10)


def move_right():
    s1.setheading(0)
    s1.forward(10)


window.onkeypress(move_for, "w")
window.onkeypress(move_down, "s")

window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# TODO - pick keys for each control


def move_fo():
    s2.setheading(90)
    s2.forward(10)


def move_dows():
    s2.setheading(270)
    s2.forward(10)

def move_lef():
    s2.setheading(180)
    s2.forward(10)


def move_righ():
    s2.setheading(0)
    s2.forward(10)


window.onkeypress(move_fo, "Up")
window.onkeypress(move_dows, "Down")

window.onkeypress(move_lef, "Left")
window.onkeypress(move_righ, "Right")


s3 = create_sprite("soccerball (1)", -10, -230)
# Section 4: Game Loop
p1_score = 0
p2_score = 0 
window.listen()
timer = 0
while True:
    time.sleep(0.1)
    timer += 1

    # TODO - code for automatic action
    if get_distance(s1, s3) < 20:
        s3.setheading(0)
        s3.forward(10)
    if get_distance(s2, s3) < 20:
        s3.setheading(180)
        s3.forward(10)
    if get_distance (s1,s3) < 20 and get_distance (s2, s3) :
        s3.setheading(90)
        s3.forward(20) 
    if s3.ycor () > -230 :
        s3.setheading(270)
        s3.forward(10)
    if s3.xcor () > 250 :
        p1_score +=1
        print("Player 1 gains a point!")
        s3.goto (-10, -230)
        s1.goto (-30, -230)
        s2.goto  (20, -230)
    if s3.xcor () < -250 :
        p2_score +=1 
        s3.goto (-10, -230)
        print("Player 2 gains a point!")
        s1.goto (-30, -230)
        s2.goto  (20, -230)
    if p1_score == 3 :
        break 
    if p2_score == 3 :
        
        break
    window.update()

    # if :
    # 	break


print("Game Over")
