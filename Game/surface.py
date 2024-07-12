'''Surface
1. Display surface (only have 1. main) > the game windows anything diaplayed goes on here
2. (regular surface (flexible amount) > essentially a single image
    (something imported, rendered text or a plain color)
    Needs to be put on display surface to be visible
    
    plain color > image > text
'''

import pygame as pg
import sys

pg.init() # Initialize all Pygame modules # It's like a start car engine

#setup the resolution and display
screen = pg.display.set_mode((800,400)) # Set windows size
pg.display.set_caption('Run Pancha')

#setup the clock and fps
clock = pg.time.Clock()
fps = 60

#setup the font with anti-aliasing
font = pg.font.SysFont('calibri',12)

test_surface = pg.Surface((100, 200))  # Create surface with width 100 and height 200
test_surface.fill((31, 120, 64))  # Fill surface with red color

#main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill((34, 54, 92))
    screen.blit(test_surface,(100,100)) #surface, position
    screen.blit(test_surface,(300,00))
    
    # Render #for clear text
      # Clear screen with background color
    
    #get and render the FPS
    fps_display = str(int(clock.get_fps()))
    fps_text = font.render(f"FPS : {fps_display}", True, pg.Color('white'))
    screen.blit(fps_text, (10,10))
    
    pg.display.flip() #update the display
    clock.tick(fps)  #cap the frame rate
    pg.display.update()
