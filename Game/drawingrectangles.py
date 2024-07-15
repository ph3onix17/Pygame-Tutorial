'''pygame.draw draw rectangles, circles, lines, points, ellipses etc'''
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
        # if event.type == pg.MOUSEMOTION:
        #     if alien_rect.collidepoint(event.pos) : print('collision')
    
    screen.blit(bg_top,(0,0))
    screen.blit(snail,snail_rect)
    screen.blit(alien,(alien_rect))
    
    #pg.draw.rect(screen,'#c0e8ec',text_rect)
    #pg.draw.rect(screen,'#c0e8ec',text_rect,10,20)
    #pg.draw.line(screen,'gold',(0,0),pg.mouse.get_pos(),10)
    #pg.draw.ellipse(screen,'blue', pg.Rect(100,200,200,200)) #pg.Rect(left,top,width,height)
    screen.blit(text_surface,(text_rect))
    
    snail_rect.x -= 4
    if snail_rect.x <= -100: snail_rect.x = 1200
    #print(alien_rect.colliderect(snail_rect)) # ***
    # if alien_rect.colliderect(snail_rect):
    #     print('collision')
    
    # mouse_pos = pg.mouse.get_pos()
    # if alien_rect.collidepoint((mouse_pos)):
    #     print(pg.mouse.get_pressed()) #boolean value of mouse buttons, left scroll right
    
    pg.display.update()
    clock.tick(60)  #cap the frame rate
    
