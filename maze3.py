import pygame

pygame.init()
screen = pygame.display.set_mode((660,660))

rectangles = [
    (0, 160, 200, 40),
    (160, 40, 40, 160),
    (160, 40, 240, 40),
    (400, 40, 40, 240),
    (80, 240, 320, 40),
    (80, 240, 40, 200),
    (200, 280, 40, 200),
    (240, 440, 240, 40),
    (480, 240, 40, 240),
    (480, 480, 160, 40),
    (600, 320, 40, 200),
    (240, 320, 160, 40),
    (250, 480, 40, 100),
    (280, 540, 100, 40),
    (340, 540, 40, 150),
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