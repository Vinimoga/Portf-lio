from turtle import *
from random import *

def init():
    speed(255)
    right(-90)
    penup()
    goto(0,-300)
    pendown()

def Tree(size, lvl, angle):

    if lvl > 0:
        forward(size)
        right(angle)
        Tree(size*0.8, lvl - 1,angle)
        lt(2 * angle)
        Tree(size*0.8, lvl - 1,angle)
        right(angle)
        bk(size)

def TreeAleatória(size, lvl, angle):
    if lvl > 0:
        forward(size)
        right(angle)
        TreeAleatória(size*uniform(0.5,1), lvl - 1,angle)
        lt(2 * angle)
        TreeAleatória(size*uniform(0.5,1), lvl - 1,angle)
        right(angle)
        bk(size)

#init()
#Tree(150, 7, 30)
#TreeAleatória(150,12,30)
#done()