import matplotlib.pyplot as plt
import numpy as np
from typing import Final, List, Tuple


Grid = Tuple[Tuple[int]]

COLOR_BG: Final[Tuple[int, int, int]] = (255, 255, 255)
COLORS: Final[List[Tuple[int, int, int]]] = [
    (0, 0, 0),
    (30, 147, 255),
    (250, 61, 49),
    (78, 204, 48),
    (255, 221, 0),
    (153, 153, 153),
    (229, 59, 163),
    (255, 133, 28),
    (136, 216, 241),
    (147, 17, 49),
]


def visualize_grid_pairs(
    grid_pairs: List[Tuple[Grid, Grid]],
    figsize: Tuple[int, int] = (10, 5)
) -> None:
    width, height, off = 0, 0, 1
    for grid_inp, grid_out in grid_pairs:
        width += len(grid_inp[0]) + len(grid_out[0]) + 5
        height = max(height, max(len(grid_inp), len(grid_out)) + 4)
    
    image = [[COLOR_BG for _ in range(width)] for _ in range(height)]
    for grid_inp, grid_out in grid_pairs:
        width_inp, width_out = len(grid_inp[0]), len(grid_out[0])
        for y, row in enumerate(grid_inp):
            for x, cell in enumerate(row):
                image[y + 2][off + x + 1] = COLORS[cell]
        off += width_inp + 1
        for y, row in enumerate(grid_out):
            for x, cell in enumerate(row):
                image[y + 2][off + x + 1] = COLORS[cell]
        off += width_out + 4
    
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(np.array(image))
    
    off = 1
    for grid_inp, grid_out in grid_pairs:
        width_inp, width_out = len(grid_inp[0]), len(grid_out[0])
        height_inp, height_out = len(grid_inp), len(grid_out)

        ax.hlines(
            [(y + 1.5) for y in range(height_inp + 1)],
            xmin=(off + 0.5),
            xmax=(off + width_inp + 0.5),
            color="black"
        )
        ax.vlines(
            [(off + x + 0.5) for x in range(width_inp + 1)],
            ymin=1.5,
            ymax=(height_inp + 1.5),
            color="black"
        )
        off += width_inp + 1

        ax.hlines(
            [(y + 1.5) for y in range(height_out + 1)],
            xmin=(off + 0.5),
            xmax=(off + width_out + 0.5),
            color="black"
        )
        ax.vlines(
            [(off + x + 0.5) for x in range(width_out + 1)],
            ymin=1.5,
            ymax=(height_out + 1.5),
            color="black"
        )
        off += width_out + 2

        ax.vlines([off + 0.5], ymin=-0.5, ymax=(height - 0.5), color="black")
        off += 2
    
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()
