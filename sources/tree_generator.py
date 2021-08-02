import numpy as np


def apply_rules(t0: np.ndarray, t1: np.ndarray):
    pass


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

    size = 500

    t0 = np.zeros((size, size), dtype=int)
    t1 = np.zeros((size, size), dtype=int)

    for i in range(0, size):
        for j in range(0, size):
            pass
