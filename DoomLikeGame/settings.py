import math
import pygame as pg

RES = WIDTH, HEIGHT = 500, 500
FPS = 60

#Ambos os Fake valores abaixos foram feitos tendo em vista diferentes resoluções de computadores
FAKEWIDTH = 50
FAKEHEIGHT = 50

PLAYER_POS = 1,1 #Mini Map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi/3
HALF_FOV = FOV/2
NUM_ARRAYS = int(WIDTH/2)
HALF_NUM_ARRAYS = NUM_ARRAYS//2
DELTA_ANGLE = FOV/NUM_ARRAYS
MAX_DEPTH = 20
GRID_BLOCK = 50


