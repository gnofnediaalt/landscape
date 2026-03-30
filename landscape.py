import pygame
import math
import random

pygame.init()

WIDTH = 600
HEIGHT = 482
SIZE = (WIDTH, HEIGHT)
#CENTER: 300, 241

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------

dt = 0
fps = 30
startup_sound = [pygame.mixer.Sound("winxp.wav"), False]

# ---------------------------

def top_hills(surface):
    points_top = []
    for x in range(0, WIDTH):
        offset = 20 * math.sin(x * 0.01 + dt / 5)
        y = 282 + offset - 40 * math.sin((x+64)/150)
        points_top.append((x, y))
    points_top.append((WIDTH, HEIGHT))
    points_top.append((0, HEIGHT))
    pygame.draw.polygon(surface, (50, 200, 50), points_top)

def bot_hills(surface, shift=0, colour=(50, 150, 50)):
    points_bot = []
    for x in range(-50+shift, WIDTH+50+shift):
        offset = 20 * math.sin(x * 0.01 + dt / 3)
        y = 482 - (((x - 250)/120) ** 3 + 85 + offset)
        points_bot.append((x-shift, y))
    points_bot.append((WIDTH+50, HEIGHT+50))
    points_bot.append((-50, HEIGHT+50))
    pygame.draw.polygon(surface, colour, points_bot)

def randomize_grass(surface):
    px = pygame.PixelArray(surface)
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            colour = surface.unmap_rgb(px[x, y])
            
            if colour.g > 140:
                r = int(colour.r * ((random.random() - 0.5) / 10 + 1))
                g = int(colour.g * ((random.random() - 0.5) / 10 + 1))
                b = int(colour.b * ((random.random() - 0.5) / 10 + 1))
                
                r = max(0, min(255, r))
                g = max(0, min(255, g))
                b = max(0, min(255, b))
                
                px[x, y] = surface.map_rgb((r, g, b))
    
    del px

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # GAME STATE UPDATES  
    if dt % 24 < 3:
        fps = 30
        screen.fill("#000000")
        if not startup_sound[1]:
            pygame.mixer.Sound.play(startup_sound[0])
            startup_sound[1] = True
        pygame.draw.rect(screen, "#FF5C01", (190, 131, 100, 100))
        pygame.draw.rect(screen, "#83C501", (310, 131, 100, 100))
        pygame.draw.rect(screen, "#00B8F8", (190, 251, 100, 100))
        pygame.draw.rect(screen, "#FFC000", (310, 251, 100, 100))

    elif dt % 24 < 15:
        if dt % 24 < 9:
            fps = 30
        elif dt % 24 < 12:
            fps = 8
        else:
            fps = 2
        screen.fill("#5581EE")
        top_hills(screen)
        bot_hills(screen, 30, (20, 70, 80))
        bot_hills(screen)
        randomize_grass(screen)
    
    elif dt % 24 < 16:
        screen.fill("#000000")
    
    else:
        screen.fill("#000082")
        
    
    # UTILITIES
    pygame.display.flip()
    dt += clock.tick(fps) / 1000
    #---------------------------

pygame.quit()
