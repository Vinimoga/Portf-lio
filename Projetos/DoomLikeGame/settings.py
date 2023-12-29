import math
import pygame as pg

RES = WIDTH, HEIGHT = 1000, 700
FPS = 60

#Fake values for different resolutions (more malleable)
FAKEWIDTH = 50
FAKEHEIGHT = 50

#Player movement
PLAYER_POS = 3,3 #Mini Map
PLAYER_ANGLE = math.pi/4

PLAYER_SPEED = 0.001
PLAYER_ROT_SPEED = 0.002

#Raycasting
FOV = math.pi/3
HALF_FOV = FOV/2
NUM_ARRAYS = int(WIDTH/2)
HALF_NUM_ARRAYS = NUM_ARRAYS//2
DELTA_ANGLE = FOV/NUM_ARRAYS
MAX_DEPTH = 20
GRID_BLOCK = 50
FLASHTIME = 2 #Seconds
MANTAINTIME = 2 #Seconds

#Mouse Movement
MOUSE_SENSITIVITY =  0.0001
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 300
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

#Pseudo 3D
SCREEN_DISTANCE = (WIDTH//2)/math.tan(HALF_FOV)
SCALE_OF_RECTANGLE = WIDTH//NUM_ARRAYS #n rectangles (numrays) times the Scale of the rectangle mus be equal to the width

#Texture
TEXTURE_SIZE = 256
see_distance = 4
