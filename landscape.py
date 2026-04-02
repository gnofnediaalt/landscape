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
crash_sound = [pygame.mixer.Sound("xpcrash.wav"), False]
try:
    pixel_font = pygame.font.Font("PixelifySans-VariableFont_wght.ttf", 16)
except pygame.error as e:
    print(f"Error loading font: {e}. Using system font.")
    pixel_font = pygame.font.SysFont(None, 16)

text_surface = pixel_font.render("A problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nPROJECT_TOO_AMAZING\n\nIf this is the first time you've seen this error screen, restart your computer. If this screen appears again, follow these steps:\n\nCheck to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.\n\nIf problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode.\n\nTechnical Infromation:\n\n*** STOP: 0x000000ED (0xMADE0000 0xBY000000 0xAIDEN000 0xFONG0000)", True, ("#FFFFFF"), wraplength=560)

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

def cloud(surface, type, position=[300, 300], scale=1, colour=[220, 220, 220]):
    offset = int(-15 * math.sin(0.9 * dt))
    cooler = []
    for i in range(len(colour)):
        cooler.append(int(max(0, min(255, (offset + colour[i])))))
    if type == "mon":
        pygame.draw.circle(surface, cooler, position, 20*scale)
    if type == "duo":
        pygame.draw.circle(surface, cooler, position, 20*scale)
        pygame.draw.circle(surface, cooler, (position[0]-20*scale, position[1]-12*scale), 14*scale)
    if type == "tri":
        pygame.draw.circle(surface, cooler, position, 20*scale)
        pygame.draw.circle(surface, cooler, (position[0]-20*scale, position[1]+8*scale), 14*scale)
        pygame.draw.circle(surface, cooler, (position[0]+20*scale, position[1]+7*scale), 16*scale)
    if type == "lin":
        pygame.draw.circle(surface, cooler, position, 15*scale)
        pygame.draw.circle(surface, cooler, (position[0]-20*scale, position[1]-8*scale), 11*scale)
        pygame.draw.circle(surface, cooler, (position[0]+20*scale, position[1]+7*scale), 13*scale)

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

def sunbeam(surface):
    px = pygame.PixelArray(surface)
    offset = math.sin(0.9 * dt) * 0.5 + 1
    denom = math.sqrt(0.3**2 + 1)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            colour = surface.unmap_rgb(px[x, y])
            if (0.2 * x + 140 <= y) and (0.4 * x + 260 >= y):
                d = abs(0.3*x - y + 200) / denom
                shade = max(0, 1 - d*offset/100) * 40
                r = int(colour.r + shade)
                g = int(colour.g + shade)
                b = int(colour.b + shade)
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
        crash_sound[1] = False

    elif dt % 24 < 17:
        if dt % 24 < 12:
            fps = 30
        elif dt % 24 < 15:
            fps = 8
        else:
            fps = 2
        screen.fill("#5581EE")
        top_hills(screen)
        bot_hills(screen, 30, (20, 70, 80))
        bot_hills(screen)
        randomize_grass(screen)
        cloud(screen, "mon", [200, 175], 0.5)
        cloud(screen, "tri", [26, 20], 0.9)
        cloud(screen, "duo", [70, 30], 0.7)
        cloud(screen, "duo", [120, 35], 0.7)
        cloud(screen, "tri", [440, 40], 1.1)
        cloud(screen, "tri", [540, 90], 1.2)
        cloud(screen, "tri", [600, 10], 1)
        cloud(screen, "duo", [560, 50], 0.8)
        cloud(screen, "lin", [500, 23], 0.8)
        cloud(screen, "lin", [250, 100], 0.9)
        cloud(screen, "lin", [290, 140], 0.6)
        cloud(screen, "duo", [440, 215], 0.8)
        cloud(screen, "tri", [480, 245], 0.8)
        cloud(screen, "duo", [480, 185], 0.8)
        cloud(screen, "lin", [540, 200], 1)
        cloud(screen, "duo", [120, 200], 0.7)
        cloud(screen, "duo", [550, 245], 0.8)
        cloud(screen, "lin", [300, 25], 0.8)
        cloud(screen, "mon", [390, 185], 0.8)
        sunbeam(screen)
    
    elif dt % 24 < 18:
        screen.fill("#000000")
        if not crash_sound[1]:
            pygame.mixer.Sound.play(crash_sound[0])
            crash_sound[1] = True
    
    else:
        screen.fill("#000082")
        screen.blit(text_surface, (25, 25))
        startup_sound[1] = False
    
    # UTILITIES
    pygame.display.flip()
    dt += clock.tick(fps) / 1000
    #---------------------------

pygame.quit()
