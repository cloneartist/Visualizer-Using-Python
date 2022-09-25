import pygame
import random
pygame.init()


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    GRADIENTS = [

        (128, 128, 128), (160, 160, 160), (192, 192, 192)
    ]
    FONT = pygame.font.SysFont('comicsans', 20)
    LARGEFONT = pygame.font.SysFont('comicsans', 30)
    SIDE_PAD = 100
    TOP_PAD = 120

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.block_width = round((self.width-self.SIDE_PAD)/len(lst))
        self.block_height = ((self.height-self.TOP_PAD) /
                             (self.max_val-self.min_val))
        self.start_x = self.SIDE_PAD//2

