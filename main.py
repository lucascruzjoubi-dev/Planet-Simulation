import pygame
import math

pygame.init()
pygame.display.set_caption("Planet Sim")
WIDTH = 600
HEIGHT = 600
center_x = WIDTH // 2
center_y = HEIGHT // 2
origin_x = 0
origin_y = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)  
DARK_GREY = (80, 78, 81)
BLUE = (100, 149, 237)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
run = True


class Planet:
    G = 6.67e-11
    AU = 149.6e6 * 1000
    SCALE = 250 / AU
    TIMESTEP = 3600 * 24
    def __init__(self, x, y, radius, color, mass, vel_y=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.sun = False
        self.orbit = []
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = vel_y

    def draw(self, screen):
        x = self.x * self.SCALE + WIDTH // 2
        y = self.y * self.SCALE + HEIGHT // 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in  self.orbit: 
                x, y = point
                x = x * self.SCALE + WIDTH // 2
                y = y * self.SCALE + HEIGHT // 2
                updated_points.append((x, y))
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

    def atraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2))

        if other.sun:
            self.distance_to_sun = distance


        force = self.G * self.mass * other.mass / math.pow(distance, 2) 
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.atraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP 

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

# class Moon:
#     AU = 149.6e6 * 1000
#     SCALE = 250 / AU
#     TIMESTEP = 3600 * 24
#     G = 6.67e-11
#     def __init__(self, parent, x, y, radius, color, mass):
#         self.x = x
#         self.y = y
#         self.parent = parent # O planeta que ela orbita (ex: earth)
#         # Distância orbital em pixels ou metros
#         self.radius = radius
#         self.color = color
#         self.angle = 0                # Ângulo atual da órbita
#         self.speed = 0.05            # Velocidade de rotação (ajuste como quiser)
#         self.orbit = []
#         self.x_vel = 0
#         self.y_vel = 0
#         self.mass = mass

#     def update_position(self, moons):
#         # Avança o ângulo da órbita
#         total_fx = total_fy = 0
#         self.angle += self.speed

#         for moon in moons:
#             if self == moon:
#                 continue

#             fx, fy = self.atraction(moon)
#             total_fx += fx
#             total_fy += fy

#         self.x_vel += total_fx / self.mass * self.TIMESTEP
#         self.y_vel += total_fy / self.mass * self.TIMESTEP 

#         self.x += self.x_vel * self.TIMESTEP
#         self.y += self.y_vel * self.TIMESTEP
#         self.orbit.append((self.x, self.y))
#         # Calcula a posição SEMPRE relativa à posição atual da Terra (parent)
#         # self.x = self.parent.x + self.distance * math.cos(self.angle)
#         # self.y = self.parent.y + self.distance * math.sin(self.angle)
        
#         # Guarda o rastro
#         self.orbit.append((self.x, self.y))
#         if len(self.orbit) > 100:  # Limita o tamanho do rastro
#             self.orbit.pop(0)

#     def draw(self, screen, parent):
#         # distance_to_earth_x = parent.x
#         # distance_to_earth_y = parent.y  
#         # parent_x, parent_y = parent.x, parent.y

#         # Aqui você usa a mesma lógica de desenho que usa para os planetas
#         # Convertendo as coordenadas reais x e y para pixels da tela
#         x = int(parent.x * self.SCALE) + WIDTH // 2
#         y = int(parent.y * self.SCALE) + HEIGHT // 2
#         # print("Values of", "x:", x, "y:", y)
            
#         if len(self.orbit) > 2:
#             updated_points = []
#             for point in self.orbit: 
#                 x, y = point
#                 x = int(parent.x * self.SCALE) + WIDTH // 2
#                 y = int(parent.y * self.SCALE) + HEIGHT // 2

#                 # print("parent.x:", parent.x, "parent.y", parent.y)

#                 updated_points.append((x, y))
#         pygame.draw.circle(screen, self.color, (x, y), self.radius)

#     def atraction(self, parent):
#         parent_x, parent_y = parent.x, parent.y
#         distance_x = parent_x - self.x
#         distance_y = parent_y - self.y
#         distance = math.sqrt(math.pow(distance_x, 2) + math.pow(distance_y, 2))

#         if parent.earth:
#             self.distance_to_earth = distance

#         force = self.G * self.mass * parent.mass / math.pow(distance, 2)
#         theta = math.atan2(distance_y, distance_x)
#         force_x = math.cos(theta) * force
#         force_y = math.sin(theta) * force
#         return force_x, force_y

#     # def distance(self, parent):
#     #     distance_to_parent_x = parent.x
#     #     distance_to_parent_y = parent.y
#     #     distance = 

def main():
    run = True
    clock = pygame.time.Clock()
    G = 6.67e-11

    sun_distance_x = WIDTH // 2
    sun_distance_y = HEIGHT // 2
    sun_distance = (sun_distance_x, sun_distance_y)

    sun = Planet(0, 0, 60, YELLOW, 1.98892e30)
    print("sun.x:", sun.x, "sun.y:", sun.y)
    sun.sun = True

    mercury_distance = 0.387 * Planet.AU
    mercury = Planet(sun_distance_x + mercury_distance, sun_distance_y, 8, DARK_GREY, 3.30e23)
    mercury.y_vel = -47.4 * 1000

    earth_distance = -1 * Planet.AU
    vel_earth = math.sqrt(G * sun.mass / earth_distance)
    earth = Planet(-1 * Planet.AU + sun_distance_x, sun_distance_y, 16, BLUE, 5.9742e24, vel_y=vel_earth)
    earth.y_vel = 29.783 * 1000
    earth.x = -1 * Planet.AU

    #Lembrar de adaptar o código para vel_relativo de cada planeta
    moon_distance = 0.00257 * Planet.AU
    moon_relative = math.sqrt(G * earth.mass / moon_distance)
    moon = Planet(earth.x + moon_distance, earth.y, 4, WHITE, 7.3476e22, vel_y= earth.vel_y+ moon_relative)

    planets = [sun, mercury, earth, moon]
    while run:

        clock.tick(60)  # limits FPS to 60
        screen.fill("black")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(screen)

        moon.atraction(earth)
        # for moon in moons:
        #     moon.update_position(moons)
        #     moon.draw(screen, parent=earth)
                
        # fill the screen with a color to wipe away anything from last frame
        # mercury = Planet(sun_distance_x, sun_distance_y, 10, mercury_mass, "grey")
    
        # flip() the display to put your work on screen
        pygame.display.update()

   
    pygame.quit()


main()