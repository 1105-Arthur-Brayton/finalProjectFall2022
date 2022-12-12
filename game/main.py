# Brayton Arthur
# sources cited
# content from kids can code: http://kidscancode.org/blog/
# Andrew helped with entity spawning
# Roman Moralez helped with Sweep class

# import libraries and modules

from settings import *
import pygame as pg
from pygame.sprite import Sprite
import random
# from random import randint

vec = pg.math.Vector2

# score
SCORE = 5

# difficulty
# DIFFICULTY = int(input("Difficulty: 0 being the easiest, 4 being the hardest: "))

# amount of enemies killed
MOBS = 0
# amount of enemies active
ENEMIES = 1
# to get rid of the hint about the space bar - press space
HINT = 0


def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

# sprites...
class Player(Sprite):
    def __init__(self):
        # defines player sprite parameters
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print("Player class")
        

    # what happens when certain keys are pressed
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_r]:
            self.pos = vec(WIDTH / 2, HEIGHT / 2) # resets position
        if keys[pg.K_LEFT]:
            self.acc.x = -2.5
        if keys[pg.K_RIGHT]:
            self.acc.x = 2.5
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE] > 0: # sets acceleration to make the player rise while held
            global HINT
            if hits and self.vel.y > 0:
                self.acc.y = 0
                self.vel.y = -.000000001
                HINT += 1 
            else:
                self.acc.y = -1.2
                HINT += 1 
        if keys[pg.K_g]:
            print("Controlls Updating")
            if keys[pg.K_g]:
                # self.pos = vec(self.rect.x, self.rect.y)
                color = TEAL
                s = Sweep(150, 150, player.rect.x, player.rect.y, color)
                all_sprites.add(s)
                sweeps.add(s)
                print("sweep")
    def update(self):
        print("Updating Sweep")
        self.blast()
               
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_platforms, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -40
    # updating all movement and acceleration and gravity
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos


class Sweep(Sprite):
    def __init__(self, w, h, x, y, color):
        # defines sweep sprite parameters
        Sprite.__init__(self)
        self.w = w
        self.h = h
        self.image = pg.Surface((300, 300))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (player.rect.x, player.rect.y)
        # self.pos = (player.pos.x, player.pos.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        print("Sweep class")
        
    # def blast(self):
    #     print("Controlls Updating")
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_g]:
    #         # self.pos = vec(self.rect.x, self.rect.y)
    #         color = TEAL
    #         s = Sweep(player.rect.x, player.rect.y, color)
    #         all_sprites.add(s)
    #         sweeps.add(s)
    #         print("sweep")
    # def update(self):
    #     print("Updating Sweep")
    #     self.blast()
    




# creates platform class
# platforms is sublass of sprite
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

'''
class Elevator(Platform(Sprite)):
    def __init__(self, lift):
        Platform.__init__(self)
        Sprite.__init__(self)
        self.lift = lift
        lift = self.vel.y
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
'''
# scrapped elevator idea        

class Enemy(Sprite):
    def __init__(self, x, y, color, w, h):
        Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.image = pg.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.pos = vec(self.x, self.y)
        
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
enemies = pg.sprite.Group()
sweeps = pg.sprite.Group()

# instantiate the player class
player = Player()
# enemy1 = Enemy(100, 200, RED, 25, 25)
# plat = Platform(x, y, width, height)
plat = Platform(WIDTH/2, HEIGHT/2 + 100, 100, 10)
plat2 = Platform(0 - WIDTH / 2, HEIGHT/1.05, WIDTH * 2, 35) # Bottom
plat3 = Platform(50, 200, 200, 10)
plat4 = Platform(800, 375, 200, 10)
plat5 = Platform(0 - WIDTH / 2, 0, WIDTH * 2, 10) # Top 
# elevator = Elevator(0, 0, 50, 100, 10)
# sweep
colors = [WHITE, RED, GREEN, BLUE]


for i in range(1):
    x = random.randint(0, WIDTH)
    y = random.randint(15, HEIGHT - 40)
    movex = random.randint(-2, 2)
    movey = random.randint(-2, 2)
    color = random.choice(colors)
    e = Enemy(x, y, color, 25, 25)
    all_sprites.add(e)
    enemies.add(e)
    print(e)
# creates the first enemy 
# source: Andrew


# add player to all sprites group
all_sprites.add(player, plat, plat2, plat3, plat4, plat5)
all_platforms.add(plat, plat2, plat3, plat4, plat5)



# # Timer
# FRAME = 1
# TIMER = 0
# RAMP = 150
# # ramp sets the time in ticks when the score will decrease

# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    
    


    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                player.jump()
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()
    all_platforms.update()
    # sweeps.update()
    hits = pg.sprite.spritecollide(player, all_platforms, False)
    kill = pg.sprite.spritecollide(player, enemies, True)
    # Begin 'spawn block'
    if kill and SCORE <= 15:
        SCORE += 1
        print("Kill")
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        MOBS += 1
        if SCORE == 15:
            ENEMIES + 1
    if kill and 15 <= SCORE <= 25: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        MOBS += 1
        if SCORE == 25:
            ENEMIES + 1
    if kill and 25 <= SCORE <= 35: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)    
        MOBS += 1
        if SCORE == 35:
            ENEMIES + 1
    if kill and 35 <= SCORE <= 45: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)  
        MOBS += 1
        if SCORE == 45:
            ENEMIES + 1
    if kill and 45 <= SCORE <= 55: 
        SCORE += 1
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT - 40)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)    
        MOBS += 1   
        if SCORE == 55:
            ENEMIES + 1       
    # every time a point threshold is crossed, even if it isn't the first time, add another enemy
    '''
    displace = pg.sprite.spritecollide(plat or plat2 or plat3 or plat4 or plat5, enemies, True)
    if displace: 
        print("Displace")
        x = random.randint(0, WIDTH)
        y = random.randint(40, HEIGHT)
        movex = random.randint(-2, 2)
        movey = random.randint(-2, 2)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
    '''
    # supposed to move enemies if they spawn inside a platform. Doesn't work. Changed parameters of enemy spawns to fix

    if player.vel.y > 0:
        if hits:
            player.pos.y = hits[0].rect.top
            player.vel.y = 0
            # negative vel means player is moving down, so when it hits a platform it needs to rest
    if player.vel.y < -.00000000001:
        if hits:
            player.rect.top = hits[0].rect.bottom
            player.vel.y = 10
            # positive vel means player is moving up, so it should be set to the bottom and make the velocity from negative to positive
    # sometimes, with enough intial velocity, the player will phase through from the bottom
    # this is because the vel.y will momentarily be zero because of the math
    # if I could use derivatives to determine the direction of the velocity, I could fix the lack of collision issues
    # currently, there is no distinction between if vel.y = 0 is from the top or bottom
    

    if FRAME % RAMP == 0 and SCORE < 15:
        SCORE -= 2
    if FRAME % RAMP == 0 and 15 < SCORE <= 25:
        SCORE -= 5
    if FRAME % RAMP == 0 and 25 < SCORE <= 35:
        SCORE -= 10
    if FRAME % RAMP == 0 and 35 < SCORE <= 45:
        SCORE -= 15    
    # if FRAME % RAMP == 0 and 45 < SCORE <= 55:
    #     SCORE -= 20
    if FRAME % RAMP == 0 and 45 < SCORE <= 55: # Instead of
        RAMP = 90
        SCORE -= 10
    # establishes the point thresholds and how many points are lost per 150 ticks
    
    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    
    draw_text("Enemies: " + str(ENEMIES), 30, WHITE, WIDTH / 4, 20)
    draw_text("Kills: " + str(MOBS), 30, WHITE, WIDTH / 4, 50)
    draw_text("POINTS: " + str(SCORE), 24, WHITE, WIDTH / 2, HEIGHT / 20)
    draw_text("Timer: " + str(int(TIMER)), 24, WHITE, WIDTH / 2, HEIGHT / 10)
    draw_text("CONTROLS", 24, WHITE, WIDTH - 150, 10)
    draw_text("Arrow keys:       Movement", 24, WHITE, WIDTH - 175, 30)   
    draw_text("R:       Reset Position", 24, WHITE, WIDTH - 116, 55)
    if HINT == 0:
        draw_text("Stuck? Question: Where might gravity not be an issue?", 24, WHITE, 500, 500)
    if HINT != 0:
        draw_text("Space:       Float", 24, WHITE, WIDTH - 176, 80)
    if SCORE >= 56:
        draw_text("You won!", 50, WHITE, WIDTH / 2, HEIGHT / 2)  
    if SCORE < 0:
        draw_text("Surprise! No stakes!", 30, WHITE, WIDTH / 2, HEIGHT / 2)
    # draws on-screen text

    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()
    FRAME += 1
    TIMER += 1 / 30
    # adds to system timer and human timer
    if SCORE >= 56:    
        TIMER = 0


    

pg.quit()
