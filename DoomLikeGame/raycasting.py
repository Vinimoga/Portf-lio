import pygame as pg
import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        #self.textures = self.game.object_renderer.wall

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, projection_height, texture, offset = values

            wall_column = self.textures[texture].subsurface(
                offset * (TEXTURE_SIZE - SCALE_OF_RECTANGLE), 0, SCALE_OF_RECTANGLE, TEXTURE_SIZE
            )

            wall_column = pg.transform.scale(wall_column, (SCALE_OF_RECTANGLE,projection_height))
            wall_pos = (ray*SCALE_OF_RECTANGLE, HEIGHT//2 - projection_height//2)

            self.objects_to_render.append((depth,wall_column,wall_pos))

    def ray_cast(self):
        self.ray_casting_result = []
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos
        ray_starting_angle = self.game.player.angle - HALF_FOV + 0.0001 #add number for division by 0 error

        texture_horizontal, texture_vertical = 1,1

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
                
                
                '''

            #check the horizontals
            y_horizontal, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 0.00000001, -1)
            # Subtracting y_map for a bigger number will result in error
            depth_horizontal = (y_horizontal - oy)/sin_a
            x_horizontal = ox + depth_horizontal * cos_a
            d_depth = dy / sin_a
            dx = d_depth * cos_a

            for count in range(MAX_DEPTH):
                tile_horizontal = int(x_horizontal), int(y_horizontal)
                if tile_horizontal in self.game.map.world_map:
                    # Ray has intersection with wall
                    texture_horizontal = self.game.map.world_map[tile_horizontal]
                    break
                x_horizontal += dx
                y_horizontal += dy

                depth_horizontal += d_depth

            # Check the verticals
            x_vertical, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 0.00000001, -1)
            #Subtracting x_map for a bigger number will result in error
            depth_vertical = (x_vertical - ox) / cos_a
            y_vertical = oy + depth_vertical * sin_a
            d_depth = dx / cos_a
            dy = d_depth * sin_a

            for count in range(MAX_DEPTH):
                tile_vertical = int(x_vertical), int(y_vertical)
                if tile_vertical in self.game.map.world_map:
                    # Ray has intersection with wall
                    texture_vertical = self.game.map.world_map[tile_vertical]
                    break
                x_vertical += dx
                y_vertical += dy

                depth_vertical += d_depth

            #Now with 2 depth, lets get the tinyest one
            #also lets see witch one of the textures should be analized
            if depth_vertical < depth_horizontal:
                depth = depth_vertical
                texture = texture_vertical
                y_vertical %= 1
                offset = y_vertical if cos_a > 0 else (1 - y_vertical)
            else:
                depth = depth_horizontal
                texture = texture_horizontal
                x_horizontal %= 1
                offset = (1 - x_horizontal) if sin_a > 0 else x_horizontal


            #debug on the 2D perpective
            #pg.draw.line(self.game.screen, 'red', (FAKEWIDTH * ox, FAKEHEIGHT * oy),
            #        (FAKEWIDTH * (ox + depth * cos_a), FAKEHEIGHT * (oy + depth * sin_a)), 2)

            #Removal of the fishbowl efect (curvature of the FOV)
            depth *= math.cos(self.game.player.angle - ray_starting_angle )


            #Projection height
            projection_height = SCREEN_DISTANCE / (depth + 0.00001) #Tiny number for division by zero error


            #Flash determination
            keys = pg.key.get_pressed()
            if keys[pg.K_r]:
                color = [(255/(1 + depth ** 5 * see_distance/1000)),0,0]
            else:
                color = [100/(1 + depth ** 5 * see_distance)] * 3
            # Draw Projection

            pg.draw.rect(self.game.screen, color ,
                         (ray * SCALE_OF_RECTANGLE, HEIGHT//2 - projection_height//2, SCALE_OF_RECTANGLE, projection_height))

            #Ray casting result

            #Changes the angle until the fov is completer with rays
            ray_starting_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()