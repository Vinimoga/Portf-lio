# libraries
import pygame
import numpy as np
# import time

# setup
pygame.init()
resolution = width,height = ((854, 480))
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
running = True
number_of_particles = 500


class Particle:
    def __init__(self, surface):
        self.pos = None
        self.color = None
        self.surface = surface
        self.radius = 5

    def get_pos(self):
        self.pos = [np.random.randint(self.radius, width - self.radius), np.random.randint(self.radius, height - self.radius)]

    def give_pos(self, pos):
        self.pos = pos

    def get_color(self):
        self.color = list(np.random.choice(range(256), size=3))

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius)

    def status(self):
        print(f'position: {self.pos}     color: {self.color}')

    def movement(self):
        pass


particulas = []
teste = False

for i in range(number_of_particles):
    copy = True
    particulas.append(Particle(screen))
    particulas[i].get_color()

    # Let's make sure we don't spawn any particle inside another.
    while copy:

        copy = False
        particulas[i].get_pos()

        print('Valor do i:', i)
        particulas[i].status()

        x, y = particulas[i].pos
        radius = particulas[i].radius

        for j in range(len(particulas)):
            if i != j:
                r = radius + particulas[j].radius
                if (x - r) < particulas[j].pos[0] < (x + r) and (y - r) < particulas[j].pos[1] < (y + r):
                    copy = True


# print(particulas) #debug

# PyGame While
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER
    for i in range(number_of_particles):
        particulas[i].draw()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
