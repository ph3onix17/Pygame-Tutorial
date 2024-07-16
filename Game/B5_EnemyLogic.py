'''
    Better enemy spawn logic (with timers)

    1. we create a list of obstacle rectangles
    2. everytime the timer triggers we add a new rectangle to that list
    3. we move every rectangle in that list to the left on every frame
    
'''
import pygame as pg
import sys

def display_score():
    current_time = pg.time.get_ticks() - start_time
    score_surface = textF.render(f'SCORE: {current_time//144}', True,(0, 150, 98))
    score_rect = score_surface.get_rect(center = (600,50))
    screen.blit(score_surface,score_rect)
    return current_time

pg.init() # Initialize
screen = pg.display.set_mode((1200,600)) # Set windows size
pg.display.set_caption('Run Kito') #title
clock = pg.time.Clock()
textF = pg.font.Font('Game/fonts/OpenSans-Bold.ttf', 30) #font type, size
text_gameover = pg.font.Font('Game/fonts/OpenSans-Bold.ttf', 30)  #font type, size
text_restart = pg.font.Font('Game/fonts/OpenSans-Bold.ttf', 30) 
game_active = True
start_time = 0
score = 0

bg_top = pg.image.load('Game/graphics/bgTop.png').convert()
bg_top = pg.transform.smoothscale(bg_top,(1200, 600))

snail = pg.image.load('Game/graphics/snail.png').convert_alpha() #easy _alpha for make png
snail = pg.transform.smoothscale(snail,(70,70))
snail = pg.transform.flip(snail, True, False)
snail_rect = snail.get_rect(bottomright = (800,396))

text_gameover = text_gameover.render('GAME OVER', True, (27, 191, 145))
text_gameover_rect = text_gameover.get_rect(center=(screen.get_width() // 2, 50))

text_restart_surface = text_restart.render('PRESS R TO RESTART', True, (27, 191, 145))
text_restart_rect = text_restart_surface.get_rect(center=(screen.get_width() // 2, 570))

alien = pg.image.load('Game/graphics/alien.png').convert_alpha()
alien = pg.transform.smoothscale(alien,(150,150))
alien_rect = alien.get_rect(topleft = (100,245))
alien_gravity = 0

#intro screen
player_stand = pg.image.load('Game/graphics/alien.png').convert_alpha()
#into single line
#player_stand = pg.transform.smoothscale(pg.image.load('Game/graphics/alien.png').convert_alpha(),size=(200,200))
player_stand = pg.transform.smoothscale(player_stand,size=(200,200))
#2x scale
#player_stand = pg.transform.scale2x(player_stand)
#rotate zoom
#player_stand = pg.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (600,300))

game_name  = textF.render('Run Kito',False,(27, 191, 145))
game_name_rect = game_name.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2 - 200))

# Timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer,900)



while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()
        
        if game_active:
            #by clicking
            if event.type == pg.MOUSEBUTTONDOWN:
                if alien_rect.collidepoint(event.pos) and alien_rect.bottom == 394:
                    alien_gravity = -25
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
                start_time = pg.time.get_ticks()
        
        if event.type == obstacle_timer and game_active:      
            print("test timer")
        
    if game_active:
        screen.blit(bg_top,(0,0))
        
        screen.blit(alien,(alien_rect))
        score = display_score()
        
        # snail_rect.x -= 7
        # if snail_rect.x <= -100: snail_rect.x = 1200
        # screen.blit(snail,snail_rect)
        
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
        screen.blit(player_stand,player_stand_rect)
        screen.blit(text_restart_surface,text_restart_rect)
        screen.blit(game_name,game_name_rect)
        
        score_message = textF.render(f'Your score: {score//144}', True, (27, 191, 145))
        score_message_rect = score_message.get_rect(center = (600, 500))
        
        if score == 0:
            screen.blit(text_gameover, text_gameover_rect)
        else:
            screen.blit(score_message, score_message_rect)
    
    pg.display.update()
    clock.tick(60)
    
