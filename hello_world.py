import pygame
from enum import Enum

pygame.init()

WIN_HEIGHT = 800
WIN_WIDTH = 800

BOARD_WIDTH = 600
BOARD_HEIGHT = 600

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.mixer.init()
pygame.mixer.music.load("royalty-free-jazz.mp3")
pygame.mixer.music.play()



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
            self.image = pygame.image.load('black.png')
        else:
            self.color = (255, 255, 255)
            self.image = pygame.image.load('white.png')

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
        pygame.draw.line(window, (138, 138, 138), [i, 1000], [i, 0], 2)
    for i in range(0, maxy, 50):
        pygame.draw.line(window, (138, 138, 138), [1000, i], [0, i], 2)
    pygame.display.update()

def game():
    global q
    while not q:
        pygame.time.delay(100)
        win.fill((0, 0, 0))
        draw_grid(win)
        win.blit(blackSheep.image, (2 + blackSheep.x, 10 + blackSheep.y))
        pygame.display.update()
        lastKey = None
        timeUp = False
        while not timeUp:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    q = True
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    lastKey = "l"
                if keys[pygame.K_RIGHT]:
                    lastKey = "r"
                if keys[pygame.K_UP]:
                    lastKey = "u"
                if keys[pygame.K_DOWN]:
                    lastKey = "d"
            break
        if lastKey == "l":
            blackSheep.x -= 50
        if lastKey == "r":
            blackSheep.x += 50
        if lastKey == "u":
            blackSheep.y -= 50
        if lastKey == "d":
            blackSheep.y += 50


#pygame.quit()


if __name__ == "__main__":
    game()

