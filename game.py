import pygame, sys
import random

class Rick(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.originalImage = pygame.image.load("pickle_rick.png")
        self.image = pygame.transform.scale(self.originalImage, (80, 100))
        self.rect = self.image.get_rect(center = (50, HEIGHT/2))
        self.pressed_keys = {"up": False, "down": False}

    def update(self):
        if self.pressed_keys["up"]:
            self.rect.y -= 5
        if self.pressed_keys["down"]:
            self.rect.y +=5

    def shoot_laser(self):
        return Laser(60, self.rect.y - 20)

class Laser(pygame.sprite.Sprite):
    def __init__(self, Xi, Yi):
        super().__init__()
        self.image = pygame.Surface((40, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (Xi, Yi + 50))

    def update(self):
        self.rect.x += 10
    
        if self.rect.x >= WIDTH + 100:
            self.kill()

class Morty(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mortyTransparent.png")
        self.rect = self.image.get_rect(center = (WIDTH, random.randint(50, 500)))
        self.children = 0

    def update(self):
        self.rect.x -= 10
        if self.rect.x < WIDTH/random.randint(4, 8):
            if self.children == 0:
                self.children = 1
                morty_group.add(Morty())

        if self.rect.x < 0:
            self.kill()

class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Alien.png")
        self.rect = self.image.get_rect(center = (WIDTH, random.randint(50, 500)))
        self.children = 0

    def update(self):
        self.rect.x -= 10
        if self.rect.x < WIDTH/random.randint(2, 6):
            if self.children < 1:
                self.children += 1
                morty_group.add(Alien())

        if self.rect.x < 0:
            self.kill()

# GAME VARIABLES

pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)

# Rick
rick = Rick()
rick_group = pygame.sprite.Group()
rick_group.add(rick)

# Laser
laser_group = pygame.sprite.Group()

# Morty
morty_group = pygame.sprite.Group()
morty_group.add(Morty())

# Aliens
alien_group = pygame.sprite.Group()
alien_group.add(Alien())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                rick.pressed_keys["up"] = True
            if event.key == pygame.K_s:
                rick.pressed_keys["down"] = True
            if event.key == pygame.K_SPACE:
                laser_group.add(rick.shoot_laser())
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                rick.pressed_keys["up"] = False
            if event.key == pygame.K_s:
                rick.pressed_keys["down"] = False

    #pygame.sprite.groupcollide(laser_group, alien_group, True, True):
    

    # Draw Objects
    screen.fill((30, 30, 30))
    laser_group.draw(screen)
    rick_group.draw(screen)
    morty_group.draw(screen)
    alien_group.draw(screen)
    rick_group.update()
    laser_group.update()
    morty_group.update()
    alien_group.update()
    pygame.display.flip()
    clock.tick(30)