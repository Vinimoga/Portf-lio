import math

RES = WIDTH, HEIGHT = 1350, 700
FPS = 60

#Ambos os Fake valores abaixos foram feitos tendo em vista diferentes resoluções de computadores
FAKEWIDTH = WIDTH/16
FAKEHEIGHT = HEIGHT/9

PLAYER_POS = 1,1 #Mini Map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002

FOV = math.pi/3
HALF_FOV = FOV/2
NUM_ARRAYS = WIDTH//2
HALF_NUM_ARRAYS = NUM_ARRAYS//2
DELTA_ANGLE = FOV/NUM_ARRAYS
MAX_DEPTH = 20


