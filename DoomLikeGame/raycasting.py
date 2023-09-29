import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self,game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        '''
        pg.draw.line(self.game.screen, (255, 255, 255), (ox * FAKEWIDTH, oy * FAKEHEIGHT),
                     (ox * FAKEWIDTH + FAKEWIDTH * math.cos(ray_angle) ,
                      oy * FAKEHEIGHT + FAKEHEIGHT * math.sin(ray_angle)))
        pg.draw.line(self.game.screen, (255, 255, 255), (ox * FAKEWIDTH, oy * FAKEHEIGHT),
                     (ox * FAKEWIDTH + FAKEWIDTH * math.cos(ray_angle + FOV),
                      oy * FAKEHEIGHT + FAKEHEIGHT * math.sin(ray_angle + FOV)))
        '''
        for ray in range(NUM_ARRAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            #print(sin_a, cos_a)
            for depth in range(MAX_DEPTH):
                target_x = ox + (cos_a * depth)
                target_y = oy + (sin_a * depth)
                future_target = ox + (cos_a * (depth+1)),oy + (sin_a * (depth+1))
                col = int(target_x)
                row = int(target_y)
                quadrado = col, row

                if quadrado in self.game.map.world_map:
                    pg.draw.line(self.game.screen, (255, 255, 0), (ox*FAKEWIDTH, oy*FAKEHEIGHT),
                                 (FAKEWIDTH * target_x, FAKEHEIGHT * target_y))

            ray_angle += DELTA_ANGLE


    def update(self):
        self.ray_cast()