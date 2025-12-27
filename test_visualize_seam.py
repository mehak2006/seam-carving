import cv2
from core.energy import compute_energy_sobel
from core.dp_seam import find_vertical_seam
from utils.visualization import overlay_vertical_seam

# Load grayscale image
img = cv2.imread("examples/test_image.jpg", cv2.IMREAD_GRAYSCALE)

# Compute seam
energy = compute_energy_sobel(img)
seam = find_vertical_seam(energy)

# Overlay seam
overlay = overlay_vertical_seam(img, seam)

# Resize for display (IMPORTANT)
display = cv2.resize(overlay, None, fx=0.25, fy=0.25)
# Show image
cv2.imshow("Seam Overlay", display)
cv2.waitKey(0)
cv2.destroyAllWindows()
