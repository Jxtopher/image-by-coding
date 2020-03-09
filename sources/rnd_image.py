#!/usr/bin/env python3

from PIL import Image
import random


def rnd_image(n: int, m: int, path_img_dst: str) -> None:
    random.seed(0)

    image = Image.new("RGB", (n, m))
    rgb_im = image.load()
    for i in range(0, n - 1):
        for j in range(0, m - 1):
            rgb_im[i, j] = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
    image.save(path_img_dst)
