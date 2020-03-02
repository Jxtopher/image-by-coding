#!/usr/bin/env python3

import sources.image_rotation as rotation
import sources.picture_inlay as inlay
import sources.rnd_image as rng
import sources.conv_to_grey as grey

if __name__ == "__main__":
    # rotation.rotation45degre(
    #     "reference_images/le_penseur.jpg", "ret_images/rotation45degre.jpg"
    # )
    # inlay.inlay(
    #     "reference_images/large black rectangle.jpg",
    #     "reference_images/small red rectangle.jpg",
    #     "ret_images/ret_inlay.jpg",
    # )
    # rng.rnd_image(
    #     400, 400, "ret_images/ret_rnd_img.jpg",
    # )
    grey.conv_to_grey(
        "reference_images/le_penseur.jpg", "ret_images/ret_in_grey.jpg"
    )
