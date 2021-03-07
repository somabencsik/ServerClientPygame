import pygame
from network import Network

width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0


class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))

    player.draw(win)
    player2.draw(win)

    pygame.display.update()


def main():
    n = Network()
    startPos = readPos(n.getPos())

    p = Player(startPos[0], startPos[1], 100, 100, (0, 200, 0))
    p2 = Player(0, 0, 100, 100, (200, 0, 0))

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(60)

        p2Pos = readPos(n.send(makePos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        p.move()
        redrawWindow(win, p, p2)

    pygame.quit()


main()
