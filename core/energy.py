# Compute pixel energy (cost matrix for DP).
# Image → Energy Map

import cv2
import numpy as np

def compute_energy_sobel(gray_img : np.ndarray) -> np.ndarray:

    """
    Compute energy map using the Sobel operator.

    Parameters

    ----------

    gray_img : np.ndarray
        Grayscale image of shape (H, W)-> input image

    Returns
    -------
    energy : np.ndarray
        Energy map of shape (H, W) -> output energy map

    """

    # Horizontal pixel differences
    grad_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)

    # Vertical pixel differences
    grad_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

    # Energy = total change at each pixel
    energy = np.abs(grad_x) + np.abs(grad_y)

    return energy

# Simple test (optional)
if __name__ == "__main__":
    img = cv2.imread("examples/test_image.jpg", cv2.IMREAD_GRAYSCALE)
    energy = compute_energy_sobel(img)

    print("Energy shape:", energy.shape)
    print("Min energy:", energy.min())
    print("Max energy:", energy.max())