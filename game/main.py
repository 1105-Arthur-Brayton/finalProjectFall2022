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

# difficulty
# DIFFICULTY = int(input("Difficulty: 0 being the easiest, 4 being the hardest: "))

# amount of enemies killed
enemies_killed = 0
# amount of enemies active
enemies_on_screen = 1
# to get rid of the hint about the space bar - press space
HINT = 0
# SWEEP_DELAY must equal zero to be used. This is a cooldown
SWEEP_DELAY = 0


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
                self.acc.y = -1.8
                HINT += 1 
        if keys[pg.K_g]:
            global SWEEP_DELAY
            if keys[pg.K_g] and SWEEP_DELAY == 0:
                # self.pos = vec(self.rect.x, self.rect.y)
                sweep.rect.center = (player.rect.x + 25, player.rect.y + 25)
                SWEEP_DELAY += 1
        if keys[pg.K_ESCAPE]:
            pg.quit() # "pygame.error: display Surface quit" Still does what it's supposed to I guess
    def update(self):
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
        self.image = pg.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (w/2, h/2)
        self.rect.center = (player.rect.x + 100000, player.rect.y + 100000)
        # self.pos = (player.pos.x, player.pos.y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        

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
pg.display.set_caption("Attack of the Cubes")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_platforms = pg.sprite.Group()
enemies = pg.sprite.Group()
sweepy = pg.sprite.Group()

# instantiate classes
player = Player()
sweep = Sweep(200, 200, player.rect.x + 100000, player.rect.y + 100000, TEAL)
plat = Platform(WIDTH/2, HEIGHT/2 + 100, 100, 10)
plat2 = Platform(0 - WIDTH / 2, HEIGHT/1.05, WIDTH * 2, 35) # Bottom
plat3 = Platform(50, 200, 200, 10)
plat4 = Platform(800, 375, 200, 10)
plat5 = Platform(0 - WIDTH / 2, 0, WIDTH * 2, 10) # Top 
# elevator = Elevator(0, 0, 50, 100, 10)
sweepy.add(sweep)

colors = [WHITE, RED, GREEN, BLUE]

# for i in range(1):
#     x = random.randint(0, WIDTH)
#     y = random.randint(15, HEIGHT - 40)
#     color = random.choice(colors)
#     s = Sweep(150, 150, -500, -500, color) # allows the sweep class to be instati
#     all_sprites.add(s)
#     enemies.add(s)
#     print(s)

for i in range(1):
    x = random.randint(0, WIDTH)
    y = random.randint(15, HEIGHT - 40)
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
    sweep_kill = pg.sprite.spritecollide(sweep, enemies, True) # why does this not work is it because sweep needs to move
  

    '''Begin 'spawn block' '''
    if kill and SCORE == 15:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    elif kill and SCORE == 25:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    elif kill and SCORE == 35:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    elif kill and SCORE == 45:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    elif kill and SCORE == 55:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1    
    # every time a point threshold is crossed, even if it isn't the first time, add another enemy
    elif kill:
        SCORE += 1
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_killed += 1 
    
    if sweep_kill and SCORE == 15:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    if sweep_kill and SCORE == 25:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    if sweep_kill and SCORE == 35:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    if sweep_kill and SCORE == 45:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1
    if sweep_kill and SCORE == 55:
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_on_screen += 1    
    # every time a point threshold is crossed, even if it isn't the first time, add another enemy
    if sweep_kill:
        SCORE += 1
        x = random.randint(15, WIDTH)
        y = random.randint(15, HEIGHT - 40)
        color = random.choice(colors)
        e = Enemy(x, y, color, 25, 25)
        all_sprites.add(e)
        enemies.add(e)
        enemies_killed += 1           
    ''' end 'spawn block'  '''
   
    if player.vel.y > 0:
        if hits:
            player.pos.y = hits[0].rect.top
            player.vel.y = 0
            # negative vel means player is moving down, so when it hits a platform it needs to rest
    if player.vel.y < -.00000000001:
        if hits:
            player.rect.top = hits[0].rect.bottom
            player.vel.y = 10
            # positive vel means player is moving up, so it should be set to the bottom and make the velocity positive
            # this does not apply while player is 'floating' with spacebar. that is by design to prevent collision issues
            # currently almost unused, but will be important if someone modifies this code and adjusts the positioning of platforms
    
    

    if FRAME % RAMP == 0 and SCORE <= 15:
        SCORE -= 2
    if FRAME % RAMP == 0 and 15 <= SCORE <= 25:
        SCORE -= 5
    if FRAME % RAMP == 0 and 25 <= SCORE <= 35:
        SCORE -= 10
    if FRAME % RAMP == 0 and 35 <= SCORE <= 45:
        SCORE -= 15    
    # if FRAME % RAMP == 0 and 45 <= SCORE <= 55:
    #     SCORE -= 20 
    '''
    Previous comment is left in to show the possible customization
    '''
    if FRAME % RAMP == 0 and 45 <= SCORE <= 55: # Lowers point penalty but increases frequency
        RAMP = 90
        SCORE -= 10
    # establishes the point thresholds and how many points are lost per 150 ticks

    if FRAME % 30 == 0:
        sweep.rect.center = (player.rect.x + 10000, player.rect.y + 10000)
        # all_sprites.remove(sweeps)
        # sweeps.remove(sweeps)
    
    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    
    draw_text("Enemies: " + str(enemies_on_screen), 30, WHITE, WIDTH / 4, 20)
    draw_text("Kills: " + str(enemies_killed), 30, WHITE, WIDTH / 4, 50)
    draw_text("POINTS: " + str(SCORE), 24, WHITE, WIDTH / 2, HEIGHT / 20)
    draw_text("Timer: " + str(int(TIMER)), 24, WHITE, WIDTH / 2, HEIGHT / 10)
    draw_text("CONTROLS", 24, WHITE, WIDTH - 150, 10)
    draw_text("Arrow keys:       Movement", 24, WHITE, WIDTH - 175, 30)   
    draw_text("R:       Reset Position", 24, WHITE, WIDTH - 116, 55)
    draw_text("G:       Sweep", 24, WHITE, WIDTH - 150, 80 )
    # if you add any controls to this section, add 25 to previous y level (80->105) and change Space: Float's to 130
    if HINT == 0:
        draw_text("Stuck? Question: Where might gravity not be an issue?", 24, WHITE, 500, 500)
    if HINT != 0:
        draw_text("Space:       Float", 24, WHITE, WIDTH - 177, 105)
    if TIMER >= 10 and HINT == 0:
        draw_text("Hint: Hold the spacebar to float.", 18, WHITE, 500, 550)
    if SCORE >= 56:
        draw_text("You won!", 50, WHITE, WIDTH / 2, HEIGHT / 2)  
    if SCORE < 0:
        draw_text("Surprise! No stakes!", 30, WHITE, WIDTH / 2, HEIGHT / 2)
    # draws on-screen text

    # draw all sprites
    sweepy.draw(screen)
    all_sprites.draw(screen)
   
    # buffer - after drawing everything, flip display
    pg.display.flip()
    FRAME += 1
    TIMER += 1 / 30
    # adds to system timer and human timer
    if SCORE >= 56:    
        TIMER = 0
        # Doesn't stop the game, just turns off timer and point decrease
    if SWEEP_DELAY > 0:
        SWEEP_DELAY -= 1 / 60
    if SWEEP_DELAY < 0:
        SWEEP_DELAY = 0
    # 


    
pg.quit()
