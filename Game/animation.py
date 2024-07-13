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
snail_x = 500

text_surface = textF.render('Run Kito', True, (27, 191, 145)) #text info, AA, color
text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
    
    screen.blit(bg_top,(0,0))
    screen.blit(snail,(snail_x,295))
    snail_x += 4
    if snail_x > 1200:
        snail_x = -100
    screen.blit(text_surface,(text_rect))
    
    pg.display.update()
    clock.tick(60)  #cap the frame rate
    
