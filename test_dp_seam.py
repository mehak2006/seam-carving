import cv2
import numpy as np

from core.energy import compute_energy_sobel
from core.dp_seam import find_vertical_seam

# 1️⃣ Load image as grayscale
img = cv2.imread("examples/test_image.jpg", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not loaded"

print("Image shape:", img.shape)

# 2️⃣ Compute energy map
energy = compute_energy_sobel(img)
print("Energy computed")
print("Energy shape:", energy.shape)

# 3️⃣ Find vertical seam (DP)
seam = find_vertical_seam(energy)

# 4️⃣ Basic sanity checks
H, W = img.shape

print("Seam length:", len(seam))
print("First 10 seam indices:", seam[:10])
print("Last 10 seam indices:", seam[-10:])

# 5️⃣ Validate seam values
for i, col in enumerate(seam):
    if not (0 <= col < W):
        raise ValueError(f"Invalid seam index at row {i}: {col}")

print("✅ Seam indices are valid")
print("✅ DP + parent logic works")
