import pygame
import math

pygame.init()

WIDTH = 600
HEIGHT = 482
SIZE = (WIDTH, HEIGHT)
#CENTER: 300, 241

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------

dt = 0
startup_sound = [pygame.mixer.Sound("winxp.wav"), False]

# ---------------------------

def hills(surface):
    points_top = []
    for x in range(0, WIDTH):
        offset = 20 * math.sin(x * 0.01 + dt / 5)
        y = 282 + offset - 40 * math.sin((x+64)/150)
        points_top.append((x, y))
    points_top.append((WIDTH, HEIGHT))
    points_top.append((0, HEIGHT))
    pygame.draw.polygon(surface, (50, 200, 50), points_top)
    
    points_bot = []
    for x in range(-50, WIDTH+50):
        offset = 20 * math.sin(x * 0.01 + dt / 3)
        y = 482 - (((x - 250)/120) ** 3 + 85 + offset)
        points_bot.append((x, y))
    points_bot.append((WIDTH+50, HEIGHT+50))
    points_bot.append((-50, HEIGHT+50))
    pygame.draw.polygon(surface, (50, 150, 50), points_bot)

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # GAME STATE UPDATES  
    if dt < 3:
        screen.fill("#000000")
        if not startup_sound[1]:
            pygame.mixer.Sound.play(startup_sound[0])
            startup_sound[1] = True
        pygame.draw.rect(screen, "#FF5C01", (190, 131, 100, 100))
        pygame.draw.rect(screen, "#83C501", (310, 131, 100, 100))
        pygame.draw.rect(screen, "#00B8F8", (190, 251, 100, 100))
        pygame.draw.rect(screen, "#FFC000", (310, 251, 100, 100))

    else:
        screen.fill("#5581EE")
        hills(screen)

    
    # UTILITIES
    pygame.display.flip()
    dt += clock.tick(30) / 1000
    #---------------------------

pygame.quit()
