#!/usr/bin/env python3

from PIL import Image


def rotation45degre(path_img_src: str, path_img_dst: str):
    im = Image.open(path_img_src)
    rgb_im = im.load()

    n = im.size[1]
    m = im.size[0]
    image = Image.new("RGB", (n, m))
    rgb_image = image.load()

    for i in range(0, n - 1):
        for j in range(0, m - 1):
            rgb_image[i, j] = rgb_im[j, i]

    image.save(path_img_dst)
