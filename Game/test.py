import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Rectangle properties
rect_width, rect_height = 50, 50
rect_x, rect_y = width // 2, height // 2
rect_speed = 5

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if the right arrow key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed

    # Clear the screen
    screen.fill(white)

    # Draw the rectangle
    pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
