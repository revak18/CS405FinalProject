import pygame
import sys

# Initialize Pygame
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Multi-screen Game")

# Define game states
STATE_MENU = 0
STATE_GAME = 1
current_state = STATE_MENU

def menu_screen():
    global current_state
    # --- Menu loop logic ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # Press Enter to start game
                current_state = STATE_GAME
    
    screen.fill((0, 100, 0)) # Green background for menu
    # Draw menu elements (buttons, text) here
    # ...

def game_screen():
    global current_state
    # --- Game loop logic ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: # Press Backspace to return to menu
                current_state = STATE_MENU
    
    screen.fill((0, 0, 100)) # Blue background for game
    # Draw game elements (player, enemies, score) here
    # ...

# Main game loop
while True:
    if current_state == STATE_MENU:
        menu_screen()
    elif current_state == STATE_GAME:
        game_screen()

    pygame.display.flip() # Update the display
    # Set frame rate with clock.tick()
