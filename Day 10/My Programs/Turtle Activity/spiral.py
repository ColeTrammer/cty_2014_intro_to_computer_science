import turtle
wm = turtle.Screen()
wn.bgcolor ("purple")
tess = turtle.Turtle()
tess.shape ("turtle")
tess.color ("black")

tess.penup()                # This is new
size = 20

   1  1n range(30):         #Leave an impression on the canvas
   tess.stamp()             #Leave an impression on the canvas
   size = size + 3          #Increase the size on every iteration
   tess.forward(size)       #Move tess along
   tess.right(24)           #   ... and turn her

   wn.exitone1ick()