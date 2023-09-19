from turtle import *

import turtle

#Make full screen
Screen().setup(1.0, 1.0)
tur = turtle.Turtle()

tur.speed(6)

tur.getscreen().bgcolor("black")
tur.color("cyan")

tur.penup()

tur.goto((-100, 200)) #Star (-200,50)

tur.pendown()

tur.speed(400)

def Frac(turtle, size, x):
    Somatorio_angular = 180 * (x - 2)
    if size <= 5:
        return
    else:
        for i in range(x):
            turtle.forward(size)
            Frac(turtle, size / 3, x) #Se quiser um efeito mais doido divide por 2 só

            turtle.right(180 - Somatorio_angular/x) #Estrela é 216

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            turtle.forward(size)
            star(turtle, size / 3)

            turtle.left(216) #Estrela é 216

#star(tur, 360)

tur.pencolor('white')
tur.speed(1000)
Frac(tur,200,5)

turtle.done()