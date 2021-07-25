from typing import List
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def square_tiling(
    matrix: np.ndarray, out_namefile: str, color: dict, size_of_square: int = 1
) -> None:
    fig = plt.figure(figsize=(len(matrix), len(matrix[0])))
    ax = fig.add_subplot(111)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rect1 = matplotlib.patches.Rectangle(
                (i * size_of_square, j * size_of_square),
                size_of_square,
                size_of_square,
                color=color[matrix[i][len(matrix) - 1 - j]],
            )
            ax.add_patch(rect1)

    plt.xlim([0, len(matrix) * size_of_square])
    plt.ylim([0, len(matrix) * size_of_square])
    plt.axis("off")
    plt.savefig(out_namefile, bbox_inches="tight")
