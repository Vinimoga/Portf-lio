from turtle import *

#Make full screen
Screen().setup(1.0, 1.0)

#Challenge 2

#Make Lines
speed(100)
for i in range(20):
  penup()
  setpos(-200,200 - 20*i)
  pendown()
  pencolor('black')
  pensize(1)
  setpos(200,200-20*i)

speed(4)

#Letter V
penup()
setpos(-150,150)
pencolor('red')
pendown()
pensize(5)
right(70)
forward(50)
left(140)
forward(50)
right(70)

#Letter I
penup()
setpos(-100,150)
pencolor('pink')
pendown()
right(90)
forward(48)
left(90)

#Letter N
penup()
setpos(-100+17,150)
pencolor('yellow')
pendown()
right(90)
forward(50)
left(150)
forward(60)
right(150)
forward(50)
left(90)

#Letter I
penup()
setpos(-35,150)
pencolor('purple')
pendown()
right(90)
forward(48)
left(90)

done()
