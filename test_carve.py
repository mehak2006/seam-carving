import cv2
from core.energy import compute_energy_sobel
from core.dp_seam import find_vertical_seam
from core.carve import remove_vertical_seam

# Load grayscale image
img = cv2.imread("examples/test_image.jpg", cv2.IMREAD_GRAYSCALE)

print("Original shape:", img.shape)

# Compute seam
energy = compute_energy_sobel(img)
seam = find_vertical_seam(energy)

# Remove seam
carved = remove_vertical_seam(img, seam)

print("Carved shape:", carved.shape)
