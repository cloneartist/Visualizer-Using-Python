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


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    controls = draw_info.FONT.render(
        "R-RESET | SPACE- Start Sorting | A- Ascending | D- Descending", 1, draw_info.BLACK)
    draw_info.window.blit(
        controls, (draw_info.width/2-controls.get_width()/2, 5))
    sorting = draw_info.FONT.render(
        "I- Insertion Sort | B- Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(
        sorting, (draw_info.width/2-sorting.get_width()/2, 35))
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = ()
    for i, val in enumerate(lst):
        x = draw_info.start_x+i*draw_info.block_width
        y = draw_info.height-(val-draw_info.min_val)*draw_info.block_height
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
            pygame.draw.rect(draw_info.window, color,
                             (x, y, draw_info.block_width, draw_info.height))


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1 = lst[j]
            num2 = lst[j+1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]

                yield True
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    lst = generate_starting_list(n, min_val, max_val)

    draw_info = DrawInformation(800, 600, lst)

    sorting = False
    ascending = True
    while run:
        clock.tick(60)
        draw(draw_info)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
