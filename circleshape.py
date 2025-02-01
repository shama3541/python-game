import pygame
import sys

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def Collision(self,Circle2):
        collide=self.position.distance_to(Circle2.position)
        if collide <= (self.radius + Circle2.radius):
            print("Game over")
            sys.exit()

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    



    def draw(self, screen):
        # sub-classes must override
        pass

    def updatetimer(self, dt):
        # sub-classes must override
        pass