# Find minimum-energy vertical seam using space-optimized DP.
# Energy Map → Vertical Seam

import numpy as np

def find_vertical_seam(energy : np.ndarray) -> list[int]:

    """
    Finds the minimum-energy vertical seam using space-optimized DP.

    Parameters
    ----------
    energy : np.ndarray
        Energy map of shape (H, W) -> input energy map

    Returns
    -------
    seam : list[int]
        seam[i] = column index of seam pixel in row i -> output vertical seam
        (In row i, which column should I remove?)

    """

    H, W = energy.shape

    # dp for previous row (space optimized)
    