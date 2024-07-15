'''The player character (alien)
        1. keyboard input
        2. jump + gravity
        3. Creating a floor
        
        1. keyboard input 
            i   pygame.key
            ii  event loop
'''
import pygame as pg
import sys

pg.init() # Initialize
screen = pg.display.set_mode((1200,600)) # Set windows size
pg.display.set_caption('Run Kito') #title
clock = pg.time.Clock()
textF = pg.font.Font('Game/fonts/RapierZero.ttf', 50) #font type, size

bg_top = pg.image.load('Game/graphics/bgTop.png').convert()
bg_top = pg.transform.smoothscale(bg_top,(1200, 600))

snail = pg.image.load('Game/graphics/snail.png').convert_alpha() #easy _alpha for make png
snail = pg.transform.smoothscale(snail,(100,100))
snail = pg.transform.flip(snail, True, False)
snail_rect = snail.get_rect(bottomright = (800,396))

text_surface = textF.render('Run Kito', True, (27, 191, 145)) #text info, AA, color
text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))

alien = pg.image.load('Game/graphics/alien.png').convert_alpha()
alien = pg.transform.smoothscale(alien,(150,150))
alien_rect = alien.get_rect(topleft = (100,245))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
        #key up and down
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print('jump')
        if event.type == pg.KEYUP:
            print('down')
        
    
    screen.blit(bg_top,(0,0))
    screen.blit(snail,snail_rect)
    screen.blit(alien,(alien_rect))
    screen.blit(text_surface,(text_rect))
    
    snail_rect.x -= 4
    if snail_rect.x <= -100: snail_rect.x = 1200
    
    # keys = pg.key.get_pressed()  # Getting keyboard input
    # if keys[pg.K_SPACE]:
    #     print('jump')
    
    pg.display.update()
    clock.tick(60)
    
