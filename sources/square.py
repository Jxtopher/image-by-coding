import numpy as np
from sources.ploter.plot_square_tiling import square_tiling


if __name__ == "__main__":
    color = {0: "blue", 1: "red"}
    checkerboard = np.zeros((10, 10), dtype=int)

    for i in range(len(checkerboard)):
        for j in range(len(checkerboard[i])):
            checkerboard[i][j] = i % 2 == j % 2
    print(checkerboard)
    square_tiling(checkerboard, "test.png", color, 10)
