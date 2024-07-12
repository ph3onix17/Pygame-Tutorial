import pygame as pg
import sys

pg.init() # Initialize all Pygame modules # It's like a start car engine

#setup the resolution and display
screen = pg.display.set_mode((1200,400)) # Set windows size
pg.display.set_caption('Run Pancha')

#setup the clock and fps
clock = pg.time.Clock()
fps = 60

#setup the font with anti-aliasing
font = pg.font.SysFont('calibri',12)

 #background color

#main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    #draw all out elements
    #update everything
    
    # Render #for clear text
    screen.fill((34, 54, 92))  # Clear screen with background color
    
    #get and render the FPS
    fps_display = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS : {fps_display}", True, pg.Color('white'))
    screen.blit(fps_text, (10,10))
    
    pg.display.flip() #update the display
    clock.tick(fps)  #cap the frame rate
    pg.display.update()
