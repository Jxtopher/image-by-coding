import numpy as np
from sources.ploter.plot_square_tiling import square_tiling


if __name__ == "__main__":
    color = {0: "blue", 1: "red"}
    square = np.zeros((10, 10), dtype=int)

    for i in range(len(square)):
        for j in range(len(square[i])):
            square[i][j] = i % 2 == j % 2
    print(square)
    square_tiling(square, "test.png", color, 10)
