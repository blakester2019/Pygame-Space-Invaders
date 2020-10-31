import pygame as pygame
import sys

# CLASSES
class Rick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rick_image = pygame.image.load("pickle_rick.png")
        self.rick_rect = self.rick_image.get_rect(center = (10, HEIGHT / 2))

    def update(self):
        self.rick_rect.center = pygame.mouse.get_pos()

    def shootLaser(self):
        return Laser(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1],)

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.laser_image = pygame.Surface((50, 20))
        self.laser_image.fill(255,0,0)
        self.laser_rect = self.laser_image.get_rect(center = (x, y))

    def update(self):
        self.rect.x += 5



# GAME OPTIONS
pygame.init()
SIZE = WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

# GROUPS
Rick = Rick()
Rick_Group = pygame.sprite.Group()
Rick_Group.add(Rick)

Laser_Group = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Laser_Group.add(Rick.shootLaser())

    # fill screen
    screen.fill((0, 0, 0))
    Rick_Group.draw(screen)
    Rick_Group.update()
    pygame.display.flip()
    clock.tick(30)