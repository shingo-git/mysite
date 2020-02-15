import pygame
from pygame.locals import *
import sys
import numpy as np
import pandas as pd

def main():
    pygame.init()

    white = (255 ,255 ,255)
    black = (0 ,0 ,0)
    (w, h) = (300, 300) #display size

    (x1, y1) = (w/4, h/4) #position
    (dx1, dy1) = (1, 0) #direction
    color = white

    count = 0
    board = pd.DataFrame(np.zeros((w,h)).astype(np.int))

    pygame.display.set_mode((w, h))
    pygame.display.set_caption("Langton's Ant")
    screen = pygame.display.get_surface()
    screen.fill(white)
    pygame.display.update()

    while(True):

        rect1 = (x1, y1, 1, 1)
        rect2 = (100,100,5,5)
        pygame.draw.rect(screen, color, rect1)
        pygame.draw.rect(screen, color, rect2)
        pygame.display.update()

        if board.iloc[int(x1),int(y1)] == 0:
            board.iloc[int(x1),int(y1)] = 1
            temp = dx1
            dx1 = -dy1
            dy1 = temp
            color = black
        else:
            board.iloc[int(x1),int(y1)] = 0
            temp = dx1
            dx1 = dy1
            dy1 = -temp
            color = white

        if x1 >= w-1:
            x1 = 1
        elif x1 <= 0:
            x1 = w-1

        if y1 >= h-1:
            y1 = 1
        elif y1 <= 0:
            y1 = h-1

        x1 = x1 + dx1
        y1 = y1 + dy1

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        count += 1
        print(count,x1,y1)

if __name__ == "__main__":
    main()
