import pygame

pygame.init()
screen = pygame.display.set_mode((660,660))

rectangles = [
    (0, 550, 150, 40), 
    (50, 50, 660, 40),
    (50, 50, 40, 200),
    (50, 210, 200, 40),
    (250, 150, 40, 100),
    (250, 120, 280, 40),
    (490, 150, 40, 260),
    (250, 600, 210, 40),
    (250, 500, 40, 100),
    (120, 500, 130, 40),
    (110, 500, 40, 50),
    (150, 250, 40, 160),
    (180, 370, 200, 40),
    (350, 370, 40, 260),
    (490, 400, 150, 40),
    
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