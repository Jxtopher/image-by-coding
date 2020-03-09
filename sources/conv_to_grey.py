#!/usr/bin/env python3

from PIL import Image

# convertir une image de couleur (path_img_src) en une image en nuance de gris (path_img_dst)
def conv_to_grey(path_img_src: str, path_img_dst: str) -> None :
    im = Image.open(path_img_src)
    rgb_im = im.load()

    n = im.size[0]
    m = im.size[1]
    image = Image.new("RGB", (n, m))
    rgb_image = image.load()

    for i in range(0, n - 1):
        for j in range(0, m - 1):
            mean = int((rgb_im[i,j][0] + rgb_im[i,j][1] + rgb_im[i,j][2]) / 3)
            rgb_image[i, j] = (mean,mean,mean)

    image.save(path_img_dst)


