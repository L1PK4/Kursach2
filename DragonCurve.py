import pygame
import math


def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

pygame.init()
ui = pygame.display.set_mode( (1000, 1000))

def code(code_):
    if int(code_) == 0:
        return [1]
    else:
        c = code(int(code_) - 1)
        c += [1] + c
        c[ len(c) - len(c) // 4 - 1] = 0
        return c


class curve(object):

    points = []
    delay = 10

    def __init__(self, points_):
        self.points = points_

    def change_delay(self, d):
        if self.delay + d > 0:
            self.delay += d
        else:
            self.delay = 0

    def draw_n(self, a):
        pygame.time.delay(self.delay)
        pygame.draw.line(ui,(0,0,0),self.points[a],self.points[a+1])

    def encode(self, n):
        i = 1
        for c in code(n - 1):
            dx = self.points[i][0] - self.points[i - 1][0]
            dy = self.points[i][1] - self.points[i - 1][1]
            if c == 1:
                self.points.append((self.points[i][0] + 3 * sign(dy), self.points[i][1] + 3 * sign(dx)))
            else:
                self.points.append((self.points[i][0] - 3 * sign(dy), self.points[i][1] - 3 * sign(dx)))
            i += 1

    def draw_p(self,n):
        self.points = []
        self.encode(n)
        pygame.time.delay(self.delay)
        for i in len(points):
            pygame.draw.line(ui,(0,0,0),self.points[i],self.points[i+1])


def main():
    dSpeed = 10
    running = True
    i = 2
    cu = curve([(500,500), (500,495)])
    cu.encode(17)
    ui.fill((255,255,255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 1
                    ui.fill((255,255,255))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dSpeed = +2
                elif event.key == pygame.K_RIGHT:
                    dSpeed = -2
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                    dSpeed = 0
        cu.change_delay(dSpeed)
        cu.draw_n(i)
        pygame.display.update()
        i += 1
if __name__ == "__main__":
    main()
