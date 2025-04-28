import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        # Check if the asteroid is small enough to split
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # Split the asteroid into two smaller asteroids
        random_angle = random.uniform(20, 50)
        asteroid_velocity1 = self.velocity.rotate(random_angle) * 1.2
        asteroid_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = asteroid_velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = asteroid_velocity2

        
  
