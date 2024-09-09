import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# vytvoř hodiny
clock = pygame.time.Clock()

# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800
# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))


class Player(pygame.sprite.Sprite):
    def __init__(self):
         super().__init__()
         self.x = 100
         self.y = 200
         self.index = 0
         self.spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha()
         self.surf = get_image(self.spritesheet, 0, 0, 15, 16, 3)
         self.rect = self.surf.get_rect(midbottom=(self.x, self.y))
         self.lives = 3


    def animation(self, direction):
        frame_count = 4

        self.index += 0.1
        if self.index >= frame_count:
            self.index = 0

        self.surf = get_image(self.spritesheet, int(self.index), direction, 15, 16, 3)

    def update(self):
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
    
    

def monster_animation():
    global monster_surf, monster_index
    monster_index += 0.1

    if monster_index > len(monster_walk):
        monster_index = 0
    monster_surf = monster_walk[int(monster_index)]

def get_image(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha()
    img.blit(sheet, (0, 0), ((frame_x * width), (frame_y * height), width, height))
    img = pygame.transform.scale(img, (width*scale, height*scale))
    img.set_colorkey((0, 0, 0))
    return img


# player_x a player_y v nové verzi kódu už řeší pouze spawn
player_x = 100
player_y = 200
player_index = 0
player_spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha()
# vytvoření surface pro postavičku hráče - načtení obrázku
player_surf = get_image(player_spritesheet, 0, 0, 15, 16, 3)

# kvůli detekci kolize nejprve vytvoříme rectangle pro hráče
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


# vytvoření surface pro postavičku monster - nepřítele - načtení obrázku
monster_walk_1 = pygame.image.load("monster_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("monster_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0

monster_surf = monster_walk[monster_index]

# kvůli detekci kolize nejprve vytvoříme rectangle pro monstrum
monster_rect = monster_surf.get_rect(midbottom=(300, 600))

# počítání životů - začátek
lives = 3

# vytvoření fontu - None znamená defaultní font, 25 je velikost
font = pygame.font.Font(None, 25)

monster_direction = "Left"

game_over = False

elapsed_time = 0

invul = False

player = Player()

# herní smyčka
while True:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    if game_over == False:
        # proměnná key, pod ní schováme stisknutou klávesu
        key = pygame.key.get_pressed()

        # pokud je stisknutá šipka doleva, atd.
        # změna ovládání - nyní pohybujeme vytvořením rectanglem
        

        # obarví obrazovku na bílo
        screen.fill((255, 255, 255))

        # renderování našeho fontu - pomocí fontu vytvoříme text, antialiasing a barvu
        text = font.render(f"Lives: {lives}", False, "#000000")

        # text vypíšeme do obrazovky
        screen.blit(text, (700, 10))

        # pohyb monstra
        if monster_rect.x <= 0:
            monster_direction = "Right"
        elif monster_rect.x >= screen_width - 50:
            monster_direction = "Left"

        if monster_direction == "Left":
            monster_rect.x -= 5
        elif monster_direction == "Right":
            monster_rect.x += 5


        if player_rect.left > screen_width:
            player_rect.right = 0
        elif player_rect.right > 0:
            player_rect.left > screen_width

        if player_rect.top > screen_height:
            player_rect.bottom = 0
        elif player_rect.bottom < 0:
            player_rect.top = screen_height

        if player_rect.bottom > screen_height:
            player_rect.top = 0
        elif player_rect.top < 0:
            player_rect.bottom = screen_height

        if player_rect.right > screen_width:
            player_rect.left = 0
        elif player_rect.left < 0:
            player_rect.right > screen_width


        
        monster_animation()
        # na screen vykresli - surface hráče, na x,y
        # screen.blit(player_surf, player_rect)
        # na screen vykresli - surface monstra, na x,y
        player.draw(screen)
        player.update()
        
        screen.blit(monster_surf, monster_rect)

        elapsed_time += clock.get_time()
        if elapsed_time > 2000:
            invul = False

        # detekce kolize a ubírání životů v případě kolize
        if player_rect.colliderect(monster_rect):
            if not invul:
                lives -= 1
                invul = True
                elapsed_time = 0


        if lives <= 0:
            game_over = True
    else:
        screen.fill((0, 0, 0))

    # updatuje vše
    pygame.display.update()

    # omez tickrate (jak rychle hra poběží) na 75 fps
    clock.tick(75)