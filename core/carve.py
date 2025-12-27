# Image + Seam → Smaller Image
import numpy as np


def remove_vertical_seam(img: np.ndarray, seam: list[int]) -> np.ndarray:
    """
    Removes a vertical seam from a grayscale image.

    Parameters
    ----------
    img : np.ndarray
        Grayscale image of shape (H, W)

    seam : list[int]
        seam[i] = column index to remove in row i

    Returns
    -------
    carved_img : np.ndarray
        Image of shape (H, W-1) with seam removed
    """

    H, W = img.shape

    # New image will have one less column
    carved_img = np.zeros((H, W - 1), dtype=img.dtype)

    for i in range(H):
        j = seam[i]

        # Copy everything except column j
        carved_img[i, :j] = img[i, :j]
        carved_img[i, j:] = img[i, j + 1:]

    return carved_img
