import sys
import pygame
import pygame.locals
import random
import math
from math import sin, cos, atan2

import maze1, maze2, maze3
import cake

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
        pygame.draw.rect(
            self.surface,
            "#4affd8",
            (self.x, self.y, random.uniform(5, 10), random.uniform(5, 10)),
        )


def path(pth: pygame.Rect, w: list[pygame.Rect]) -> bool:
    edges = [pth.topleft, pth.topright, pth.bottomleft, pth.bottomright]
    for edge in edges:
        in_path = False
        for rectangle in w:
            if rectangle.collidepoint(edge):
                in_path = True
                break
        if in_path == False:
            return False
    return True
    


def explosion(bull_x: float, bull_y: float, bull_r: float, ob_x: float, ob_y: float, ob_w: float, ob_h: float, bits: list[Bit], screen: pygame.Surface) -> bool:
    center_x = ob_x + ob_w / 2
    center_y = ob_y + ob_h / 2

    hit = False

    if (bull_x - center_x) ** 2 + (bull_y - center_y) ** 2 <= bull_r ** 2:
        hit = True

    if hit:
        for i in range(20):
            bits.append(Bit(screen, center_x, center_y))
        return True
    else:
        return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bullets, bits = [], []
    player = pygame.Rect(0, 0, 20, 20)

    levels = [
        (maze1.rectangles, (30, 30), pygame.Rect(620, 460, 30, 30), [(55, 200, 100, 15), (400, 420, 15, 120)]),
        (maze2.rectangles, (30, 560), pygame.Rect(620, 55, 30, 30), [(180, 470, 15, 100), (120, 320, 100, 15), (500, 30, 15, 80)]),
        (maze3.rectangles, (10, 170), pygame.Rect(345, 610, 30, 30), [(50,120,15,100), (180,400,100,15), (300, 520, 15, 100)]),
    ]

    i = 0
    rects, start, goal, obs = levels[i]
    walk = [pygame.Rect(x, y, w, h) for (x, y, w, h) in rects]
    player.topleft = start

    shoot_noise = pygame.mixer.Sound('/Users/revakhaire/Documents/CS405FinalProject/Shoot8.wav')
    coin_noise = pygame.mixer.Sound('/Users/revakhaire/Documents/CS405FinalProject/Pickup5.wav')

    while True:
        screen.fill("#000000")

        for (x, y, w_, h_) in rects:
            pygame.draw.rect(screen, "#ffffff", (x, y, w_, h_))

        for (x, y, w_, h_) in obs:
            pygame.draw.rect(screen, "#3db000", (x, y, w_, h_))

        pygame.draw.rect(screen, "#ffea00", (goal.x, goal.y, goal.w, goal.h))
        pygame.draw.rect(screen, "#fc1eae", (player.x, player.y, player.w, player.h))

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                mx, my = pygame.mouse.get_pos()
                angle = atan2(HEIGHT - my, WIDTH - mx)
                shot_x = WIDTH - 130 * cos(angle)
                shot_y = HEIGHT - 130 * sin(angle)
                vx = -10 * cos(angle)
                vy = -10 * sin(angle)
                bullets.append(Bullet(screen, shot_x, shot_y, vx, vy))
                shoot_noise.play()

        keys = pygame.key.get_pressed()
        delx = 0
        dely = 0
        vel = 5
        if keys[pygame.K_LEFT]:
            delx = -vel
        if keys[pygame.K_RIGHT]:
            delx = vel
        if keys[pygame.K_UP]:
            dely = -vel
        if keys[pygame.K_DOWN]:
            dely = vel

        prev_px = player.topleft
        player.x += delx

        hit_ob = False
        for (x, y, w, h) in obs:
            ob_rect = pygame.Rect(x, y, w, h)
            if player.colliderect(ob_rect):
                hit_ob = True
                break

        if path(player, walk) == False or hit_ob == True:
            player.topleft = prev_px

        prev_py = player.topleft
        player.y += dely

        hit_ob = False
        for (x, y, w, h) in obs:
            ob_rect = pygame.Rect(x, y, w, h)
            if player.colliderect(ob_rect):
                hit_ob = True
                break

        if path(player, walk) == False or hit_ob == True:
            player.topleft = prev_py

        mx, my = pygame.mouse.get_pos()
        angle = atan2(HEIGHT - my, WIDTH - mx)
        pygame.draw.circle(screen, "#63c3ff", (WIDTH - int(100 * cos(angle)), HEIGHT - int(100 * sin(angle))), 20)
        pygame.draw.circle(screen, "#63c3ff", (WIDTH - int(75 * cos(angle)), HEIGHT - int(75 * sin(angle))), 25)

        for b in bullets.copy():
            b.update()

            for ob in obs.copy():
                ob_x, ob_y, ob_w, ob_h = ob
                if explosion(b.x, b.y, b.radius, ob_x, ob_y, ob_w, ob_h, bits, screen) == True:
                    obs.remove(ob)

            b.display()
            if b.offscreen():
                bullets.remove(b)

        for bit in bits:
            bit.update()
            bit.display()

        if player.colliderect(goal):
            coin_noise.play()
            i += 1
            bullets.clear()
            bits.clear()
            if i >= len(levels):
                pygame.quit()
                cake.main()
                sys.exit()
            rects, start, goal, obs = levels[i]
            walk = [pygame.Rect(x, y, w_, h_) for (x, y, w_, h_) in rects]
            player.topleft = start

        if i == 0:
            font = pygame.font.SysFont("bodoni72", 20)

            obj_text = font.render("Objective: Get the gold coin!", True, "#ffffff")
            arrow_text = font.render("Move using the arrow keys!", True, "#ffffff")
            space_text = font.render("Shoot with the space bar!", True, "#ffffff")

            screen.blit(obj_text, (230, 20))
            screen.blit(arrow_text, (235, 50))
            screen.blit(space_text, (240, 80))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
