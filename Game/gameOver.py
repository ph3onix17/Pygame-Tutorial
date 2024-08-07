'''
game over if alien touches the snail
'''
import pygame as pg
import sys

pg.init() # Initialize
screen = pg.display.set_mode((1200,600)) # Set windows size
pg.display.set_caption('Run Kito') #title
clock = pg.time.Clock()
textF = pg.font.Font('Game/fonts/RapierZero.ttf', 50) #font type, size
text_gameover = pg.font.SysFont('arial', 50) #font type, size
text_restart = pg.font.SysFont('Arial',40)
game_active = True

bg_top = pg.image.load('Game/graphics/bgTop.png').convert()
bg_top = pg.transform.smoothscale(bg_top,(1200, 600))

snail = pg.image.load('Game/graphics/snail.png').convert_alpha() #easy _alpha for make png
snail = pg.transform.smoothscale(snail,(70,70))
snail = pg.transform.flip(snail, True, False)
snail_rect = snail.get_rect(bottomright = (800,396))

text_surface = textF.render('Run Kito', True, (27, 191, 145)) #text info, AA, color
text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))

text_gameover = text_gameover.render('GAME OVER', True, (27, 191, 145))
text_gameover_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))

text_restart_surface = text_restart.render('PRESS R TO RESTART', True, (27, 191, 145))
text_restart_rect = text_restart_surface.get_rect(center=(screen.get_width() // 2, 300))

alien = pg.image.load('Game/graphics/alien.png').convert_alpha()
alien = pg.transform.smoothscale(alien,(150,150))
alien_rect = alien.get_rect(topleft = (100,245))
alien_gravity = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
        
        if game_active:
            #by clicking
            if event.type == pg.MOUSEBUTTONDOWN:
                if alien_rect.collidepoint(event.pos) and alien_rect.bottom == 394:
                    alien_gravity = -20
            #key up and down
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and alien_rect.bottom == 394:
                    alien_gravity = -22
            if event.type == pg.KEYUP:
                print('down')
        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                game_active = True
                snail_rect.left = 1200
                
        
    if game_active:
        screen.blit(bg_top,(0,0))
        screen.blit(snail,snail_rect)
        screen.blit(alien,(alien_rect))
        screen.blit(text_surface,(text_rect))
        
        snail_rect.x -= 7
        if snail_rect.x <= -100: snail_rect.x = 1200
        
        #alien
        alien_gravity += 1
        alien_rect.y += alien_gravity
        if alien_rect.bottom >= 394: 
            alien_rect.bottom = 394
        screen.blit(alien,alien_rect)
        
        #collison
        if snail_rect.colliderect(alien_rect):
            game_active = False
    else:
        screen.fill('#29537d')
        screen.blit(text_gameover,text_gameover_rect)
        screen.blit(text_restart_surface,text_restart_rect)
        
    #print(pg.mouse.get_pos())
    pg.display.update()
    clock.tick(60)
    
