import pygame
from pygame.locals import *
import sys

import numpy as np
import pandas as pd

import sub_ant

def main():
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    (w, h) = (200,200)      #display_size
    (x, y) = (w/2,h/2)      #ant_position
    (dx, dy) = (1, 0)       #ant_direction

    color = white
    count = 0
    board = pd.DataFrame(np.zeros((w,h)).astype(np.int))

    pygame.display.set_mode((w, h))
    pygame.display.set_caption("Langton's Ant")
    screen = pygame.display.get_surface()
    screen.fill(white)
    pygame.display.update()

    while(True):

        ans = sub_ant.ant_plot(board, w, h, x, y, dx, dy)
        (board, x, y, dx, dy, color) = ans      #1行でも可

        pygame.draw.rect(screen, color, (x, y, 1, 1))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        count += 1
        print(count,x,y)

if __name__ == "__main__":
    main()
