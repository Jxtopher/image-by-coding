from PIL import Image
import math


def inlay(path_large_img_src: str, path_small_img_src: str, path_img_dst: str):

    image_back = Image.open(path_large_img_src)  # Le fond
    image = Image.open(path_small_img_src)  # A ajouter !

    image_back_pix = image_back.load()
    image_pix = image.load()

    print(image_pix[0, 0])

    max_x_back, max_y_back = image_back.size
    max_x_pix, max_y_pix = image.size

    center_x = max_x_pix / 2
    center_y = max_y_pix / 2

    # superposition 1 des deux images -> Haut droit
    for i in range(0, max_x_back):
        for j in range(0, max_y_back):
            if i < max_x_pix and j < max_y_pix:
                # image_back_pix[i, j] = image_pix[i, j]

                # calcul du cercle
                if (
                    math.sqrt(
                        abs(i - center_x) * abs(i - center_x)
                        + abs(j - center_y) * abs(j - center_y)
                    )
                    < center_y
                ):
                    image_back_pix[i, j] = image_pix[i, j]

    image_back.save(path_img_dst, "jpeg")
