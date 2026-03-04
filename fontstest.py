import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Mouse Position Example')

# Set up the font for displaying text
font = pygame.font.Font(None, 36)

# fonts = pygame.font.get_fonts()
# for f in fonts:
#    print(f)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Get the current mouse position
    x, y = pygame.mouse.get_pos()

    # Render the mouse position text
    text = font.render(f'Position: ({x}, {y})', True, (0, 0, 0))

    # Draw the text on the screen
    screen.blit(text, (20, 20))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()