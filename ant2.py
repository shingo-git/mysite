import pygame
from pygame.locals import *
import sys

import random
import numpy as np
import pandas as pd

import sub_ant

def main():
    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)
    lime = (0, 255, 0)
    navy = (0, 0, 128)
    red = (255, 0, 0)
    purple = (128, 0, 128)

    #display_size
    (w, h) = (200,200)

    #ant_position
    (x1, y1) = (int(w*random.random()),int(h*random.random()))
    (x2, y2) = (int(w*random.random()),int(h*random.random()))
    (x3, y3) = (int(w*random.random()),int(h*random.random()))
    (x4, y4) = (int(w*random.random()),int(h*random.random()))

    #ant_direction
    (dx1, dy1) = (1, 0)
    (dx2, dy2) = (0, 1)
    (dx3, dy3) = (-1, 0)
    (dx4, dy4) = (0, -1)

    color1 = white
    color2 = white
    color3 = white
    color4 = white

    count = 0
    board = pd.DataFrame(np.zeros((w,h)).astype(np.int))

    pygame.display.set_mode((w, h))
    pygame.display.set_caption("Langton's Ant")
    screen = pygame.display.get_surface()
    screen.fill(white)
    pygame.display.update()

    while(True):

        ans1 = sub_ant.ant_plot(board, w, h, x1, y1, dx1, dy1)
        (board, x1, y1, dx1, dy1, color1) = ans1      #1行でも可

        ans2 = sub_ant.ant_plot(board, w, h, x2, y2, dx2, dy2)
        (board, x2, y2, dx2, dy2, color2) = ans2      #1行でも可

        ans3 = sub_ant.ant_plot(board, w, h, x3, y3, dx3, dy3)
        (board, x3, y3, dx3, dy3, color3) = ans3      #1行でも可

        ans4 = sub_ant.ant_plot(board, w, h, x4, y4, dx4, dy4)
        (board, x4, y4, dx4, dy4, color4) = ans4      #1行でも可

        if color1 == black:
            color1 = lime
        if color2 == black:
            color2 = navy
        if color3 == black:
            color3 = red
        if color4 == black:
            color4 = purple

        pygame.draw.rect(screen, color1, (x1, y1, 1, 1))
        pygame.draw.rect(screen, color2, (x2, y2, 1, 1))
        pygame.draw.rect(screen, color3, (x3, y3, 1, 1))
        pygame.draw.rect(screen, color4, (x4, y4, 1, 1))
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
        print(count)

if __name__ == "__main__":
    main()
