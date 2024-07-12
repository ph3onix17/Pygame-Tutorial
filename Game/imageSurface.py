import pygame as pg
import sys

pg.init() # Initialize all Pygame modules # It's like a start car engine
screen = pg.display.set_mode((1200,600)) # Set windows size
pg.display.set_caption('Run Kito')
clock = pg.time.Clock()


bg_top = pg.image.load('Game/graphics/bgTop.png')
bg_top = pg.transform.scale(bg_top,(1200, 600))
snail = pg.image.load('Game/graphics/snail.png')
snail = pg.transform.scale(snail,(40,40))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
    
    screen.blit(bg_top,(0,0))
    screen.blit(snail,(900,354))
    pg.display.update()
    clock.tick(60)  #cap the frame rate
    
