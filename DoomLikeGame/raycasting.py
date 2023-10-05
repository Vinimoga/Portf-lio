import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_starting_angle = self.game.player.angle - HALF_FOV + 0.0001 #Adiciona um numerinho para não ter divisão por 0

        for ray in range(NUM_ARRAYS):
            sin_a = math.sin(ray_starting_angle)
            cos_a = math.cos(ray_starting_angle)
            flag = 0
            #print(sin_a, cos_a)
            '''
            for depth in range(MAX_DEPTH):
                target_x = ox + (cos_a * depth)
                target_y = oy + (sin_a * depth)
                #future_target = ox + (cos_a * (depth+1)),oy + (sin_a * (depth+1))
                col = int(target_x)
                row = int(target_y)
                quadrado = col, row

                #############################################################################################
                #Se você quiser fazer com que seja possívelandar q nem uma aranha use:
                
                if quadrado in self.game.map.world_map and flag == 0:
                    flag = 1
                    pg.draw.line(self.game.screen, (255, 255, 0), (ox*FAKEWIDTH, oy*FAKEHEIGHT),
                                 (FAKEWIDTH * col, FAKEHEIGHT * row))
                                 
                #Mude também o FOV e a quandidade de rays pois não vai ser necessário tantos rays e é melhor 
                #que haja com campo maior de 270 a 360 graus
                #############################################################################################
                
                if quadrado in self.game.map.world_map and flag == 0:
                    flag = 1
                    pg.draw.line(self.game.screen, (255, 255, 0), (ox*FAKEWIDTH, oy*FAKEHEIGHT),
                                 (FAKEWIDTH * target_x, FAKEHEIGHT * target_y))
                
                #########################################################################################################
                '''
            #check the horizontals
            y_horizontal, dy = (y_map + 1, 1) if sin_a > 0 else (y_map, -1)
            depth_horizontal = (y_horizontal - oy)/sin_a
            x_horizontal = ox + (depth_horizontal * cos_a)
            d_depth = dy / sin_a
            dx = d_depth * cos_a

            for count in range(MAX_DEPTH):
                tile_horizontal = int(x_horizontal), int(y_horizontal)
                if tile_horizontal in self.game.map.world_map:
                    # Ray has intersection with wall
                    break
                y_horizontal += dy
                x_horizontal += dx
                depth_horizontal += d_depth

                # Check the verticals
            x_vertical, dx = (x_map + 1, 1) if cos_a > 0 else (x_map, -1)

            depth_vertical = (x_vertical - ox) / cos_a
            y_vertical = oy + (depth_vertical * sin_a)

            d_depth = dx / cos_a
            dy = d_depth * sin_a

            for count in range(MAX_DEPTH):
                tile_vertical = int(x_vertical), int(y_vertical)
                if tile_vertical in self.game.map.world_map:
                    # Ray has intersection with wall
                    break
                x_vertical += dx
                y_vertical += dy

                depth_vertical += d_depth

            #Now with 2 depth, lets get the tinyest one
            if depth_vertical < depth_horizontal:
                depth = depth_vertical
            else:
                depth = depth_horizontal

            '''
                #horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor
            '''
            #debug
            pg.draw.line(self.game.screen,'red',(50*ox,50*oy),
                    (50*ox + 50*depth*cos_a,50*oy + 50*depth*sin_a),2)

            ray_starting_angle += DELTA_ANGLE

    def align(self, x, y):
        return (x // GRID_BLOCK) * GRID_BLOCK, (y // GRID_BLOCK) * GRID_BLOCK

    def update(self):
        self.ray_cast()