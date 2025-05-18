import pygame
from circleshape import CircleShape
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            ## Debugging:
            # print(f"Small asteroid (radius={self.radius}) destroyed")
            return 
        else:
            new_trajectory = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(new_trajectory) * 1.2
            velocity2 = self.velocity.rotate(-new_trajectory) * 1.2
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            ## Debugging:
            # print(f"Split asteroid: radius{self.radius}, new_radius={split_radius}, angle={new_trajectory}")
            # print(f"New velocities: {velocity1}, {velocity2}")
            asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid_1.velocity = velocity1
            asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
            asteroid_2.velocity = velocity2

    def update(self, dt):
        self.position += (self.velocity * dt)