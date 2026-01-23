import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    
    def update(self, dt):
        self.position += self.velocity * dt








# /*
# class CircleShape(pygame.sprite.Sprite):
#     def __init__(self, x, y, radius):
#         # we will be using this later
#         if hasattr(self, "containers"):
#             super().__init__(self.containers)
#         else:
#             super().__init__()

#         self.position = pygame.Vector2(x, y)
#         self.velocity = pygame.Vector2(0, 0)
#         self.radius = radius
# */