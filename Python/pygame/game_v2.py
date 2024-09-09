import pygame
from sys import exit

# import všech částí kódu hry - nastavení (výška, šířka), pomocné funkce (get_image), classu hráče, classu monstra
from settings import *
from utility import get_image
from player import Player
from monster import Monster
from level import Level


# inicializuje hru - spustíme pygame
pygame.init()

# vytvoř hodiny
clock = pygame.time.Clock()


# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))


# počítání životů - začátek
lives = 3

# vytvoření fontu - None znamená defaultní font, 25 je velikost
font = pygame.font.Font(None, 25)


# stav hry
game_over = False


# vytvoření hráče
player = pygame.sprite.GroupSingle()
player.add(Player())

# vytvoření monstra
monsters = pygame.sprite.Group()
monster = Monster()
monsters.add(monster)

desks = pygame.sprite.Group()

# vytvoření světa
level = Level("assets/tiled/ucebna2.tmx", screen, desks)
level.draw_background()


# herní smyčka
while True:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    if game_over == False:
             

        # obarví obrazovku na bílo
        level.draw_background()

        # renderování našeho fontu - pomocí fontu vytvoříme text, antialiasing a barvu
        text = font.render(f"Lives: {player.sprite.lives}", False, "#000000")

        # text vypíšeme do obrazovky
        screen.blit(text, (700, 10))



        # monster.draw(screen) vykreslí hráče
        # monster.update() updatuje jeho chování        
        monster.draw(screen)
        monster.update()

        player.draw(screen)
        player.update(monsters)
        
        player.sprite.invul_time += clock.get_time()

        desks.draw(screen)

        # detekce kolize a ubírání životů v případě kolize

        # TODO kolizi opravíme v příští hodině v pátek v 15.3.

        # if player.rect.colliderect(monster_rect):
        #     if not invul:
        #         lives -= 1
        #         invul = True
        #         elapsed_time = 0


        if lives <= 0:
            game_over = True
    else:
        screen.fill((0, 0, 0))

    # updatuje vše
    pygame.display.update()

    # omez tickrate (jak rychle hra poběží) na 60 fps
    clock.tick(75)