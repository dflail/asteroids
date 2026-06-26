import pygame
import logger
import random
import circleshape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SPLIT_ACCEL

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            split_angle = random.uniform(20.0, 50.0)
            new_vel_1 = pygame.math.Vector2.rotate(self.velocity, split_angle)
            new_vel_2 = pygame.math.Vector2.rotate(self.velocity, -split_angle)
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            split_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_1.velocity = new_vel_1 * SPLIT_ACCEL
            split_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_asteroid_2.velocity = new_vel_2 * SPLIT_ACCEL

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt