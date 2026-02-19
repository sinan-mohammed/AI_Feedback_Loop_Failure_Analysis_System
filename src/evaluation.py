import numpy as np

def verify_outputs(image, gt, pred):
    print("Image:", image.shape)
    print("GT   :", gt.shape)
    print("Pred :", pred.shape)

    assert image.shape == gt.shape == pred.shape, "Shape mismatch!"
    print("Verification passed.")
