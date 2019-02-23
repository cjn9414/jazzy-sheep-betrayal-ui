import pygame
from enum import Enum

pygame.init()

WIN_HEIGHT = 800
WIN_WIDTH = 800

BOARD_WIDTH = 600
BOARD_HEIGHT = 600

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption("Jazzy Sheep Betrayal")

q = False


class Orientation(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


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


def game():
    global q
    while not q:
        pygame.draw.rect(win, (255, 255, 255), (200, 200, 400, 400))
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

        pygame.draw.circle(win, blackSheep.color, (blackSheep.x, blackSheep.y), blackSheep.w)
        pygame.display.update()


#pygame.quit()


if __name__ == "__main__":
    game()

