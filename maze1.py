import pygame

pygame.init()
screen = pygame.display.set_mode((660,660))

rectangles = [
    (25, 0, 50, 120), 
    (40, 70, 180, 50),
    (80, 100, 50, 180),
    (80, 200, 50, 200),
    (80, 380, 200, 50),
    (250, 300, 50, 300),
    (50, 600, 250, 50),
    (250, 250, 300, 50),
    (500, 50, 50, 320),
    (300, 450, 360, 50),
    (300, 120, 200, 50),    
]

if __name__ == "__main__":
    running = True
    while running:

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        screen.fill(("#000000"))

        for rect in rectangles:
            pygame.draw.rect(screen, "#e1e1e1", rect)

        pygame.display.flip()

    pygame.quit()