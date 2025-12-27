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
    prev = energy[H - 1].copy()

    # to reconstruct the seam, we need to store the choices
    parent = np.zeros((H, W), dtype=np.int32)

    # move upwards from last row

    for i in range(H - 2, -1, -1):
        temp = np.zeros(W)

        for j in range(W):

            l = prev[j - 1] if j > 0 else 1e9
            c = prev[j]
            r = prev[j + 1] if j < W - 1 else 1e9

            best = min(l, c, r)

            # store where we go next
            if best == l:
                parent[i][j] = j - 1
            elif best == c:
                parent[i][j] = j
            else:
                parent[i][j] = j + 1

            temp[j] = energy[i][j] + best

        prev = temp

    # choose best start in top row
    j = np.argmin(prev)

    # reconstruct seam (top → bottom)
    seam = [j]
    for i in range(0, H - 1):
        j = parent[i][j]
        seam.append(j)

    return seam


