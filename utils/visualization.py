import numpy as np
import cv2


def overlay_vertical_seam(gray_img: np.ndarray, seam: list[int]) -> np.ndarray:
    """
    Overlays a vertical seam on a grayscale image.

    Parameters
    ----------
    gray_img : np.ndarray
        Grayscale image of shape (H, W)

    seam : list[int]
        seam[i] = column index of seam pixel in row i

    Returns
    -------
    overlay_img : np.ndarray
        Color image with seam highlighted in red
    """

    H, W = gray_img.shape

    # Convert grayscale to BGR so we can draw color
    overlay_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)

    # Draw seam
    for i in range(H):
        j = seam[i]
        overlay_img[i, j] = (0, 0, 255)  # Red in BGR

    return overlay_img
