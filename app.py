import streamlit as st
import cv2
import numpy as np

from core.energy import compute_energy_sobel
from core.dp_seam import find_vertical_seam
from core.carve import remove_vertical_seam
from utils.visualization import overlay_vertical_seam


st.set_page_config(page_title="Seam Carving (DP)", layout="wide")
st.title("Seam Carving using Dynamic Programming")

st.markdown(
    """
This app demonstrates **content-aware image resizing** using  
**Dynamic Programming (Minimum Falling Path Sum – LC 931)**.
"""
)

# ---- Image Upload ----
uploaded_file = st.file_uploader(
    "Upload a SMALL image (recommended width < 800px)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Decode uploaded image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_color = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Convert to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(img_gray, clamp=True)


    # ---- Controls ----
    max_seams = img_gray.shape[1] - 1
    num_seams = st.slider(
        "Number of vertical seams to remove",
        min_value=1,
        max_value=min(200, max_seams),
        value=min(50, max_seams),
        step=1
    )

    show_seam = st.checkbox("Show first seam overlay", value=True)

    # ---- Seam Carving ----
    img = img_gray.copy()

    progress = st.progress(0)

    for i in range(num_seams):
        energy = compute_energy_sobel(img)
        seam = find_vertical_seam(energy)

        if i == 0 and show_seam:
            overlay = overlay_vertical_seam(img, seam)
            st.subheader("Minimum Energy Seam (First Iteration)")
            st.image(overlay, channels="BGR")

        img = remove_vertical_seam(img, seam)
        progress.progress((i + 1) / num_seams)

    with col2:
        st.subheader("Carved Image")
        st.image(img, clamp=True)

