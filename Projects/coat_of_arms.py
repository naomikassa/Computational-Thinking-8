###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("spring")

q1 = codesters.Circle(100, 100, 200, 'white')
q2 = codesters.Circle(-100, 100, 200, 'blue')
q3 = codesters.Circle(-100, -100, 200, 'black')
q4 = codesters.Circle(100, -100, 200, 'SeaGreen')

s1 = codesters.Sprite("pinetree", 100, 100)
s1.set_size(0.5)

s2 = codesters.Sprite("flower2", -100, -100)

s3 = codesters.Sprite("spaceneedle (1)", 100, -100)
s3.set_size(0.4)

s4 = codesters.Sprite("goldendoodle (1)", -100, 100)
s4.set_size(0.4)

message1 = codesters.Text("Naomi Kassa",0, 220, "purple" )
message2 = codesters.Text("God 1st",0, -220, "DarkSlateBlue")