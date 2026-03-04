import sys
import pygame
import pygame.locals
import random
import math
from math import sin, cos, atan2

WIDTH, HEIGHT = 660, 660

class Bullet:
    def __init__(self, surface: pygame.Surface, x: float, y: float, vx: float, vy: float):
        self.surface = surface
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = 8

    def update(self) -> None:
        self.x += self.vx
        self.y += self.vy

    def display(self) -> None:
        pygame.draw.circle(self.surface, "#3731d7", (int(self.x), int(self.y)), self.radius)

    def offscreen(self):
        if self.x < -50 or self.x > WIDTH + 50 or self.y < -50 or self.y > HEIGHT + 50:
            return True

class Bit:
    def __init__(self, surface: pygame.Surface, x: float, y: float):
        self.surface = surface
        self.x = x
        self.y = y

        bit_speed = random.uniform(5, 10)
        angle = random.uniform(0, 2 * math.pi)
        self.vx = bit_speed * cos(angle)
        self.vy = bit_speed * sin(angle)

    def update(self) -> None:
        self.x += self.vx
        self.y += self.vy

    def display(self) -> None:
        pygame.draw.rect(self.surface, "#4affd8", (self.x, self.y, random.uniform(5, 10), random.uniform(5, 10)))

        # pygame.draw.rect(surface, color, (column * rect_width, row * rect_height, rect_width + 1, rect_height + 1))
        # (x, y, width, height)

# def dist(x1: float, x2: float, y1: float, y2: float):
#     return ((x2-x1)**2 + (y2-y1)**2)**0.5

# def touching(bull_x: float, bull_y: float, bull_rad: float, ob_x: float, ob_y: float, width: float, height: float):
#     ob_left = ob_x
#     ob_right = ob_x + width
#     ob_bottom = ob_y - height
#     ob_top = ob_y

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont(None, 36)

    bullets: list[Bullet] = []
    bullet_speed = 10

    bits: list[Bit] = []

    obstacles = [
    (250, 250, 160, 90),
    (100, 400, 120, 60),
    (420, 120, 140, 80)]

    def explosion(bull_x: float, bull_y: float, bull_r: float, ob_x: float, ob_y: float, ob_w: float, ob_h: float) -> bool:
        center_x = ob_x + ob_w/2
        center_y = ob_y + ob_h/2

        hit = False

        if (bull_x - center_x) ** 2 + (bull_y - center_y) ** 2 <= bull_r ** 2:
            hit = True

        if hit:
            for i in range(20):
                bits.append(Bit(screen, center_x, center_y))
            return True
        else:
            return False
    while True:
        screen.fill("#000000")
    
        for ob_param in obstacles:
            pygame.draw.rect(screen, "#2bd46a", ob_param)

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mx, my = pygame.mouse.get_pos()

                angle = atan2(HEIGHT - my, WIDTH - mx)
                shot_x = WIDTH - 130 * cos(angle)
                shot_y = HEIGHT - 130 * sin(angle)
                vx = - 10 * cos(angle)
                vy = - 10 * sin(angle)

                bullets.append(Bullet(screen, shot_x, shot_y, vx, vy))

        mx, my = pygame.mouse.get_pos()
        # text = font.render(f"Position: ({mx}, {my})", True, "#ffffff")
        # screen.blit(text, (20, 20))
       
        angle = atan2(HEIGHT - my, WIDTH - mx)
        pygame.draw.circle(screen, "#63c3ff", (WIDTH - int(100 * cos(angle)), HEIGHT - int(100 * sin(angle))), 20)
        pygame.draw.circle(screen, "#63c3ff", (WIDTH - int(75 * cos(angle)), HEIGHT - int(75 * sin(angle))), 25)

        for bullet in bullets.copy():
            bullet.update()
            
            for ob_param in obstacles.copy():
                ob_x, ob_y, ob_w, ob_h = ob_param
                if explosion(bullet.x, bullet.y, bullet.radius, ob_x, ob_y, ob_w, ob_h) == True:
                    obstacles.remove(ob_param)

            bullet.display()
            if bullet.offscreen():
                bullets.remove(bullet)

        for bit in bits:
            bit.update()
            bit.display()

        pygame.display.flip()
        fps_clock.tick(fps)

if __name__ == "__main__":
    main()