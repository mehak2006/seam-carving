import cv2
from core.energy import compute_energy_sobel
from core.dp_seam import find_vertical_seam
from core.carve import remove_vertical_seam

# Load grayscale image
img = cv2.imread("examples/test_image.jpg", cv2.IMREAD_GRAYSCALE)

print("Original shape:", img.shape)

num_seams = 100   # 👈 change this to 50, 100, 200 etc.

for i in range(num_seams):
    energy = compute_energy_sobel(img)
    seam = find_vertical_seam(energy)
    img = remove_vertical_seam(img, seam)

    if (i + 1) % 10 == 0:
        print(f"Removed {i+1} seams")

print("Final shape:", img.shape)

# Resize for display
display = cv2.resize(img, None, fx=0.25, fy=0.25)

cv2.imshow("After Seam Carving", display)
cv2.waitKey(0)
cv2.destroyAllWindows()
