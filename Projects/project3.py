import turtle
t = turtle.Turtle()
turtle.Screen (). bgcolor ("black") #black background
t.color("pink")
t.speed ( 10 ) #setting the speed higher to make it take less time- i set it to 10#


#my 3 colors
colors = ["white", "gray", "black"]
#only 20 times so the shape is more visible
for i in range (50) :
    t.color(colors[i % 3] )
    t.forward(100)
    t.left(61) 
    # 61 because I don't want it to be too big


#this is going to both grow and rotate
# I also repeated it 1000 times so that it could get really big#
colors = [ "white", "grey"]
for i in range (1000) :
    t.color(colors[ i % 2])
    t.forward(100 + i)
    t.left(61)

turtle.exitonclick()


