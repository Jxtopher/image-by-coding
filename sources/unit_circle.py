import cmath
import matplotlib.pyplot as plt
import numpy as np
import math

if __name__ == "__main__":
    center = complex(0, 0)

    x = [center.imag]
    y = [center.real]
    for i in np.arange(0, 2 * math.pi, 0.01):
        z = center + cmath.exp(complex(0, i))

        x.append(z.imag)
        y.append(z.real)

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.scatter(
        x,
        y,
    )
    # plt.axis("off")
    plt.savefig("unit_circle.png", bbox_inches="tight")
