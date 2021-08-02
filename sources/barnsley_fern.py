import numpy as np
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar


if __name__ == "__main__":
    A1 = np.array([[0, 0], [0, 0.16]])
    B1 = np.array([[0.85, 0.04], [-0.04, 0.85]])
    B2 = np.array([[0], [1.6]])
    C1 = np.array([[0.2, -0.26], [0.23, 0.22]])
    C2 = np.array([[0], [1.6]])
    D1 = np.array([[-0.15, 0.28], [0.26, 0.24]])
    D2 = np.array([[0], [0.44]])

    init = np.array([[0], [0]])

    iterations = 500000

    current = init
    x = []
    y = []
    bar = IncrementalBar("Compute", max=iterations)
    for _ in range(iterations):
        p = np.random.uniform(0, 1)
        if p > 0 and p <= 0.01:
            new = np.dot(A1, current)
        elif p > 0.01 and p <= 0.85:
            new = np.add(np.dot(B1, current), B2)
        elif p > 0.85 and p <= 0.86:
            new = np.add(np.dot(C1, current), C2)
        elif p > 0.86 and p <= 1:
            new = np.add(np.dot(D1, current), D2)
        x.append(new[0][0])
        y.append(new[1][0])
        bar.next()

        current = new
        
    fig = plt.figure(figsize=(20, 20))
    ax = fig.add_subplot(111)
    ax.scatter(x, y, s=[0.2], marker="o", color="#00BFFF")
    plt.axis("off")
    plt.savefig("barnsley_fern_image.png", bbox_inches="tight")
