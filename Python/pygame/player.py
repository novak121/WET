# class Player, která obsahuje všechny věci k hráči, jeho vlastnosti, informace a funkce

import pygame
from utility import get_image
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.x = 100
         self.y = 200
         self.index = 0
         self.spritesheet = pygame.image.load("assets/player/man_brownhair_run.png").convert_alpha()
         self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
         self.rect = self.image.get_rect(midbottom=(self.x, self.y))
         self.lives = 3

# class Player, která obsahuje všechny věci k hráči, jeho vlastnosti, informace a funkce

import pygame
from utility import get_image
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.x = 100
         self.y = 200
         self.index = 0
         self.spritesheet = pygame.image.load("../assets/player/man_brownhair_run.png").convert_alpha()
         self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
         self.rect = self.image.get_rect(midbottom=(self.x, self.y))
         
         self.lives = 3
         self.invul = False
         self.invul_time = 0



    def animation(self, direction):
        frame_count = 4

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0

        self.image = get_image(self.spritesheet, int(self.index), direction, 15, 16, 3)

        
    def update(self, monsters):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
            self.animation(2)
        elif key[pygame.K_RIGHT]:
            self.rect.x += 10
            self.animation(3)
        elif key[pygame.K_UP]:
            self.rect.y -= 10
            self.animation(1)
        elif key[pygame.K_DOWN]:
            self.rect.y += 10
            self.animation(0)
        
        if self.rect.x < 0:
            self.rect.x = screen_width - 10
        elif self.rect.x > screen_width:
            self.rect.x = 10
        
        if self.rect.y < 0:
            self.rect.y = screen_height - 10
        elif self.rect.y > screen_height:
            self.rect.y = 10

        if pygame.sprite.spritecollide(self, monsters, False):
             if not self.invul:
                print("kolize!!!!")
                self.lives -= 1
                self.invul = True
                self.invul_time = 0

        if self.invul_time > 2000:
            self.invul = False
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)