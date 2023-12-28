# libraries
from Particle import *

# import time

# setup
pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()


class Particle_System:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.running = True
        self.particle_creation()

    @staticmethod
    def particle_creation():

        for i in range(number_of_particles):
            copy = True
            particulas.append(Particle(screen))
            particulas[i].get_color()
            particulas[i].get_velocity()

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
                        x1, y1 = particulas[j].pos
                        if (x - r) < x1 < (x + r) and (y - r) < y1 < (y + r):  # Basically collision detection
                            copy = True

    def simulation(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER
        for i in range(number_of_particles):
            particulas[i].draw()
            self.detect_collision()
            particulas[i].movement()
            # time.sleep(0)
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    def detect_collision(self):
        for i in range(number_of_particles):
            x1, y1 = particulas[i].pos
            radius = particulas[i].radius

            if not ((x1 + radius + particulas[i].velocity[0]) < width) or not (
                    0 < (x1 - radius + particulas[i].velocity[0])):
                particulas[i].velocity[0] *= -1
                # print('out of bounds X')

            if not ((y1 + radius + particulas[i].velocity[1]) < height) or not (
                    0 < (y1 - radius + particulas[i].velocity[1])):
                particulas[i].velocity[1] *= -1
                # print('out of bounds Y')
'''
            for j in range(len(particulas)):
                x2, y2 = particulas[j].pos
                distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)
                if i != j:
                    
                    #r = radius + particulas[j].radius
                    #if (x1 - r) < particulas[j].pos[0] < (x1 + r) and (y1 - r) < particulas[j].pos[1] < (y1 + r):  # Basically collision detection
                    
                    print('Valor do i:', i, 'valor do j:', j, 'distância', distance)

'''
system = Particle_System()
while system.running:
    system.simulation()

pygame.quit()  # end
