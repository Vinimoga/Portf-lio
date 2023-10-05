import math
import pygame as pg

RES = WIDTH, HEIGHT = 500, 500
FPS = 60

#Fake values for different resolutions (more malleable)
FAKEWIDTH = 50
FAKEHEIGHT = 50

#Player movement
PLAYER_POS = 1,1 #Mini Map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

#Raycasting
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_ARRAYS = int(WIDTH/2)
HALF_NUM_ARRAYS = NUM_ARRAYS//2
DELTA_ANGLE = FOV/NUM_ARRAYS
MAX_DEPTH = 20
GRID_BLOCK = 50

#Pseudo 3D
SCREEN_DISTANCE = (WIDTH//2)/math.tan(HALF_FOV)
SCALE_OF_RECTANGLE = WIDTH//NUM_ARRAYS #n rectangles (numrays) times the Scale of the rectangle mus be equal to the width
