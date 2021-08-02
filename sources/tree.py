import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = [[4, 8], [6, 4]]
    y = [[8, 9], [5, 6]]

    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.plot(x, y, markersize=1, marker="o", color="black")
    # plt.axis("off")
    plt.savefig("barnsley_fern_image.png", bbox_inches="tight")
