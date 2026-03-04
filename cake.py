import sys

import pygame
import pygame.locals


WIDTH, HEIGHT = 660, 660


def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    while True:
        screen.fill("#000000")

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, "#ad6a6e", (int((screen.get_width() - 500) / 2), 550, 500, 30))

        pygame.draw.rect(screen, "#dec0a0", (int((screen.get_width() - 450) / 2), 520, 450, 30))
        pygame.draw.rect(screen, "#e1a38f", (int((screen.get_width() - 450) / 2), 500, 450, 20))
        pygame.draw.rect(screen, "#dec0a0", (int((screen.get_width() - 450) / 2), 420, 450, 80))
        pygame.draw.rect(screen, "#ff87ad", (int((screen.get_width() - 450) / 2), 390, 450, 30))
        pygame.draw.rect(screen, "#ff87ad", (int((screen.get_width() - 400) / 2), 360, 400, 30))

        pygame.draw.rect(screen, "#dec0a0", (int((screen.get_width() - 300) / 2), 330, 300, 30))
        pygame.draw.rect(screen, "#e1a38f", (int((screen.get_width() - 300) / 2), 310, 300, 20))
        pygame.draw.rect(screen, "#dec0a0", (int((screen.get_width() - 300) / 2), 250, 300, 60))
        pygame.draw.rect(screen, "#ff87ad", (int((screen.get_width() - 300) / 2), 220, 300, 30))
        pygame.draw.rect(screen, "#ff87ad", (int((screen.get_width() - 200) / 2), 190, 200, 30))

        pygame.draw.rect(screen, "#ffcfea", (275, 122, 20, 70))
        pygame.draw.rect(screen, "#ffff4d", (270, 102, 30, 20))
        pygame.draw.rect(screen, "#ffff4d", (277, 92, 15, 10))

        pygame.draw.rect(screen, "#ffcfea", (320, 122, 20, 70))
        pygame.draw.rect(screen, "#ffff4d", (315, 102, 30, 20))
        pygame.draw.rect(screen, "#ffff4d", (322, 92, 15, 10))

        pygame.draw.rect(screen, "#ffcfea", (365, 122, 20, 70))
        pygame.draw.rect(screen, "#ffff4d", (360, 102, 30, 20))
        pygame.draw.rect(screen, "#ffff4d", (367, 92, 15, 10))

        font = pygame.font.SysFont("bodoni72", 40)

        text1 = font.render("Congratulations!", True, "#8c3aff")
        text2 = font.render("You beat the mazes!", True, "#8c3aff")

        text1_rect = text1.get_rect(center=(WIDTH // 2, 280))
        text2_rect = text2.get_rect(center=(WIDTH // 2, 460))
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()