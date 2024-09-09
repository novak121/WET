import pygame
from items import Desk
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self, level_data):
        self.data = load_pygame(level_data)
        self.ground = self.data.get_layer_by_name("ground")
        self.background = pygame.Surface((self.data.screen_width * self.data.tilewidth,))
        self.screen = screen
        
        self.draw_background()

    def draw_background(self):
        for x,y, image in self.ground.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0,0))
        
        
        
    def create_desk(self):
        for desk in self.furniture:
            new_desk = Desk(desk.image, desk.width, desk.height, (desk.x, desk.y))

path = "assets/tiled/ucebna2.tmx"
level = Level(path)