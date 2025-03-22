import streamlit as st
import cv2
import numpy as np
from PIL import Image
import opencv_detect

st.title("🚧 Pothole Detection App")
st.write("Upload an image to detect potholes using OpenCV.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = np.array(Image.open(uploaded_file))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    result_image = opencv_detect.detect_potholes(image)
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    st.image(result_image, caption="Detected Potholes", use_column_width=True)

st.write("🔹 Built with OpenCV & Streamlit")
