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
    def __init__(self, points_):
        self.points = points_
    def draw(self, a):
        # pygame.time.delay(3)
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
def main():
    running = True
    i = 1
    cu = curve([(500,500), (500,495)])
    cu.encode(40)
    ui.fill((255,255,255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    i = 1
                    ui.fill((255,255,255))
        cu.draw(i)
        pygame.display.update()
        if i % 100000 == 0:
            print(i)
        i += 1
if __name__ == "__main__":
    main()
