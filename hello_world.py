import pygame
import os
from enum import Enum

pygame.init()

WIN_HEIGHT = 800
WIN_WIDTH = 800

BOARD_WIDTH = 600
BOARD_HEIGHT = 600

current_path = os.path.dirname(__file__) # Where your .py file is located
resource_path = os.path.join(current_path, 'pictures') # The resource folder path
bs_path = os.path.join(resource_path, 'black_sheep.jpg')
bs = pygame.image.load(bs_path)
bs = pygame.transform.scale(bs, (100, 100))

illum_path = os.path.join(resource_path, 'illuminated.png') # The image folder path
illum = pygame.image.load(illum_path)
illum = pygame.transform.scale(illum, (200, 200))

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Jazzy Sheep Betrayal")

q = False


class Orientation(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


def draw_grid(window):
    maxx = 1000
    maxy = 1000
    for i in range(0, maxx, 50):
        pygame.draw.line(window,(138, 138,138), [i, 1000], [i, 0], 2)
    for i in range(0, maxy, 50):
        pygame.draw.line(window, (138, 138, 138), [1000, i], [0, i], 2)
    pygame.display.update()


class Sheep:
    def __init__(self, black, x, y):
        if black:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)
        self.x = x
        self.y = y
        self.w = 25
        self.h = 25
        self.orient = Orientation.RIGHT

blackSheep = Sheep(True, 400, 400)

def draw_grid(window):
    maxx = 1000
    maxy = 1000
    for i in range(0, maxx, 50):
        pygame.draw.line(window,(138, 138,138), [i, 1000], [i, 0], 2)
    for i in range(0, maxy, 50):
        pygame.draw.line(window, (138, 138, 138), [1000, i], [0, i], 2)
    pygame.display.update()

def game():
    global q
    draw_grid(win)
    while not q:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                q = True
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                blackSheep.x -= 25
                blackSheep.orient = Orientation.LEFT
            if keys[pygame.K_RIGHT]:
                blackSheep.x += 25
                blackSheep.orient = Orientation.RIGHT
            if keys[pygame.K_UP]:
                blackSheep.y -= 25
                blackSheep.orient = Orientation.UP
            if keys[pygame.K_DOWN]:
                blackSheep.y += 25
                blackSheep.orient = Orientation.DOWN

        pygame.draw.rect(win, (255, 255, 255), (200, 200, 400, 400))
        pygame.time.delay(100)

        filter = pygame.surface.Surface((BOARD_WIDTH, BOARD_HEIGHT))

        filter.fill(pygame.color.Color('white'))
        filter.blit(illum, (blackSheep.x-100, blackSheep.y-100))
        pygame.display.flip()
        win.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        pygame.draw.circle(win, blackSheep.color, (blackSheep.x, blackSheep.y), blackSheep.w)
        pygame.display.update()


if __name__ == "__main__":
    game()

