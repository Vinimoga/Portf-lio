import pygame as pg
import math
from settings import *

class raycasting:
    def __init__(self,game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map,y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for ray in range(NUM_ARRAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.sin(ray_angle)

            #Vertical



            #Horizontal
            ray_angle += DELTA_ANGLE


    def update(self):
        self.ray_cast()