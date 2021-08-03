import matplotlib.pyplot as plt
import cmath
import math


def right(c: complex) -> complex:
    return c + cmath.exp(complex(0, math.pi / 4))


def left(c: complex) -> complex:
    return c + cmath.exp(complex(0, 3 * math.pi / 4))


if __name__ == "__main__":
    # x = [[4, 8], [6, 4]]
    # y = [[8, 9], [5, 6]]

    p = complex(0, 0)
    x = [[p.real, p.real], [left(p).real, right(p).real]]
    y = [[p.imag, p.imag], [left(p).imag, right(p).imag]]

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.plot(x, y, markersize=1, marker="o", color="black")
    # plt.axis("off")
    plt.savefig("test.png", bbox_inches="tight")
