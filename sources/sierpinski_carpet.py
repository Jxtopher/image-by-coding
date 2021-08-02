from typing import List
import matplotlib
import matplotlib.pyplot as plt


class Square:
    def __init__(
        self, center: bool, x: float, y: float, width: float, height: float
    ) -> None:
        self.center = center
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def generateCarpet(square: Square) -> List[Square]:
    squares = []

    width = square.width / 3
    height = square.height / 3
    for i in range(3):
        x = square.x + width * i
        for j in range(3):
            y = square.y + width * j
            if i == 1 and j == 1:
                squares.append(Square(True, x, y, width, height))
            else:
                squares.append(Square(False, x, y, width, height))
    return squares


def plot(squares: List[Square], out_namefile):
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111)

    for item in squares:
        if item.center:
            rect1 = matplotlib.patches.Rectangle(
                (item.x, item.y), item.width, item.height, color="black"
            )
        else:
            rect1 = matplotlib.patches.Rectangle(
                (item.x, item.y), item.width, item.height, color="white"
            )
        ax.add_patch(rect1)

    plt.xlim([0, 200])
    plt.ylim([0, 200])
    plt.axis("off")
    plt.savefig(out_namefile, bbox_inches="tight")


if __name__ == "__main__":
    square = Square(False, 0, 0, 200, 200)
    all_squares = []
    depth = 10

    current = []
    current.append(square)
    for i in range(depth):
        squares = []
        for item in current:
            squares += generateCarpet(item)
        all_squares += squares
        current.clear()
        for item in squares:
            if not item.center:
                current.append(item)
    plot(all_squares, "test.png")
