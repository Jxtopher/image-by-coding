from typing import List
from PIL import Image
from copy import deepcopy
import numpy as np
from numpy.matrixlib.defmatrix import matrix
from sources.ploter.plot_square_tiling import square_tiling


def apply_rules(rules: List[dict], line: List, new_line: List, num_case: int) -> None:
    for rule in rules:
        if (
            rule["pattern"][0] == line[num_case - 1]
            and rule["pattern"][1] == line[num_case]
            and rule["pattern"][2] == line[num_case + 1]
        ):
            new_line[num_case] = rule["new_state"]
            break


if __name__ == "__main__":
    rules_num_90 = [
        {"pattern": [1, 1, 1], "new_state": 0},
        {"pattern": [1, 1, 0], "new_state": 1},
        {"pattern": [1, 0, 1], "new_state": 0},
        {"pattern": [1, 0, 0], "new_state": 1},
        {"pattern": [0, 1, 1], "new_state": 1},
        {"pattern": [0, 1, 0], "new_state": 0},
        {"pattern": [0, 0, 1], "new_state": 1},
        {"pattern": [0, 0, 0], "new_state": 0},
    ]

    # color = {
    #     "red": (255, 0, 0),
    #     "white": (255, 255, 255),
    #     "black": (0, 0, 0),
    #     "aero_blue": (202, 241, 222),
    #     "picton_blue": (75, 177, 249),
    #     "amber": (255, 125, 3),
    #     "catalina_blue": (0, 51, 119),
    #     "papaya_whip": (254, 243, 215),
    # }
    color = {0: "#062a78", 1: "#ffbf00"}

    n = 200
    matrix = np.zeros(shape=(n, n), dtype=int)

    line_t0 = np.array([0] * n)
    line_t1 = np.array([0] * n)

    line_t0[round(n / 2)] = 1

    matrix[0] = deepcopy(line_t0)

    for num_line in range(1, n - 1):
        for i in range(1, n - 1):
            apply_rules(rules_num_90, line_t0, line_t1, i)

        matrix[num_line] = deepcopy(line_t1)
        line_t0 = deepcopy(line_t1)

    square_tiling(matrix, "test.png", color, 10)
