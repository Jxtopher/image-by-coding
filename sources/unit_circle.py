import cmath
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import math


def plot1() -> None:
    center = complex(0, 0)

    x = []
    y = []
    for i in np.arange(0, 2 * math.pi, 0.05):
        z = center + cmath.exp(complex(0, i))

        x.append(z.imag)
        y.append(z.real)

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.scatter(x, y, s=[1])
    plt.title(r"$z = e^{i\theta}$")
    plt.savefig("unit_circle.png", bbox_inches="tight")


if __name__ == "__main__":
    plot1()
