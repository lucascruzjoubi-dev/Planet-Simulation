import pygame
import math

pygame.init()
pygame.display.set_caption("Planet Sim")
WIDTH = 600
HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


sun_pos = WIDTH / 2, HEIGHT / 2
sun_pos_x = WIDTH / 2
sun_pos_y = HEIGHT / 2
orbit_radius = 100
sun_distance_x = sun_pos_x + orbit_radius
sun_distance_y = sun_pos_y + orbit_radius
angle = 0
angle_speed = 0.03



class Planet:
    G = 6.67e-11
    AU = 149.6e6 * 1000
    SCALE = 250 / AU
    def __init__(self, x, y, radius, mass, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        # self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in  self.orbit: 
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

    def atraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = abs(other_x - self.x)
        distance_y = abs(other_y - self.y)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    mercury_x = sun_pos_x + orbit_radius * math.cos(angle)  
    mercury_y = sun_pos_y + orbit_radius * math.sin(angle)
    
    angle += angle_speed

    pygame.draw.circle(screen, "orange", sun_pos, 30)
    pygame.draw.circle(screen, "grey", (int(mercury_x), int(mercury_y)), 10)

    # mercury = Planet(sun_distance_x, sun_distance_y, 10, mercury_mass, "grey")
  
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()