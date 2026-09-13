import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if  self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        vel = self.velocity.rotate(angle)
        vel_neg = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = vel * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid.velocity = vel_neg * 1.2
