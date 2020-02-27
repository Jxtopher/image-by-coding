#!/usr/bin/env python3

import sources.image_rotation as rotation
import sources.picture_inlay as inlay

if __name__ == "__main__":
    rotation.rotation45degre(
        "reference_images/le_penseur.jpg", "ret_images/rotation45degre.jpg"
    )
    inlay.inlay(
        "reference_images/large black rectangle.jpg",
        "reference_images/small red rectangle.jpg",
        "ret_images/ret_inlay.jpg",
    )
