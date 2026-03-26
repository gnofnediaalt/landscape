import pygame
import math

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------

circle_x = 200
circle_y = 200
dt = 0

# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # GAME STATE UPDATES
    screen.fill(("#000000"))
    circle_x += 10
    circle_y = math.sin(circle_x / 40) * 100 + 200
    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)
    pygame.draw.circle(screen, (200, 200, 10), ((math.sin(dt)*200+240), (math.sin(dt)*200+240)), 20)

    if circle_x > 800:
        circle_x = -100
    
    # UTILITIES
    pygame.display.flip()
    dt += clock.tick(30)/1000
    #---------------------------

pygame.quit()
