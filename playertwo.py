import sys

import pygame
import pygame.locals

from math import sin, cos, tan, atan

WIDTH, HEIGHT = 750, 750

# # Set up the font for displaying text
 
class Bullet:
    def __init__(self, surface: pygame.Surface, x: float, y: float, m_x: float, m_y: float):
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.m_x = m_x
        self.m_y = m_y

    def update(self) -> None:

        vector_x = self.m_x - self.x
        vector_y = self.m_y - self.y
        v_mag = (vector_x**2 + vector_y**2)**0.5
        keys_held = pygame.key.get_pressed()

        if keys_held[pygame.K_SPACE]:
             self.vx = v_mag / vector_x
             if vector_y == 0:
                self.vy = 0
             else:
                cself.vy = v_mag / vector_y
             
        self.x += self.vx 
        self.y += self.vy 

    def display(self) -> None:
        pygame.draw.circle(self.surface, "#3731d7", (self.x, self.y), 10)
        # vx = 0
        # vy = 0

        # keys_held = pygame.key.get_pressed()

        # if keys_held[pygame.K_RIGHT]:
        #      vx = 5

        # shot_x += vx

        # pygame.draw.circle(screen, "#313cd7", (shot_x, shot_y), 10)
 
def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    font = pygame.font.SysFont(None, 36)

    while True:
        screen.fill("#8C8888")

        # up_pressed = False
        # down_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_UP:
            #         up_pressed = True
            #         down_pressed = False
            #     elif event.key == pygame.K_DOWN:
            #         up_pressed = False
            #         down_pressed = True

        # # Get the current mouse position
        x, y = pygame.mouse.get_pos()

        # # Render the mouse position text
        text = font.render(f'Position: ({x}, {y})', True, "#ffffff")

        # # Draw the text on the screen
        screen.blit(text, (20, 20))

        if x <= 0:
            x = 1
        elif x >= 750:
            x = 750
        
        if y >= 750:
            y = 750
        angle = atan(y/x)
        
        pygame.draw.circle(screen, "#d73153", (130 * cos(angle), 130 * sin(angle)), 20)
        pygame.draw.circle(screen, "#d73153", (100 * cos(angle), 100 * sin(angle)), 25)


        shot_x = 130 * cos(angle)
        shot_y = 130 * sin(angle)
        projectile = Bullet(screen, shot_x, shot_y, x, y)

        projectile.update()
        projectile.display()

        '''split'''

        # if up_pressed:
        #     pygame.draw.circle(screen, "#d73153", (705, 705), 40)
        # elif down_pressed:
        #     pygame.draw.circle(screen, "#d73153", (705, 45), 40)

        # Update the display
        pygame.display.flip()
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()

