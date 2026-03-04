import sys

import pygame
import pygame.locals


WIDTH, HEIGHT = 500, 500


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        screen.fill("#33b744")

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.draw.circle(screen,"#ffffff", (250,250), 50)

        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()