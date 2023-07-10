import pygame

# Initialize pygame
pygame.init()

# Set display surface
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pygame Template')

# Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# Set game values

# Set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set fonts

# Set text

# Set sounds

# Set images


# The main game loop
running = True
while running:
    # Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

    # Fill the display surface
    display_surface.fill(BLACK)

    # Blit assets to the display surface

    # Update the display
    pygame.display.update()
    clock.tick(FPS)


# End the game
pygame.quit()