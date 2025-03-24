import streamlit as st
import cv2
import numpy as np
from PIL import Image
import opencv_detect
import yolo_detect

st.title("🚧 Pothole Detection App")
st.write("Upload an image to detect potholes using OpenCV and YOLO.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if st.button("Process with Opencv"):
     if uploaded_file is not None:
        image = np.array(Image.open(uploaded_file))
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        result_image_1 = opencv_detect.detect_potholes(image)
        result_image_1 = cv2.cvtColor(result_image_1, cv2.COLOR_BGR2RGB)
        st.image(result_image_1, caption="Detected Potholes", use_column_width=True)

if st.button("Process with YOLO"):
    if uploaded_file is not None:
        image_2=Image.open(uploaded_file)
        result_image_2 =  yolo_detect.detect_potholes(image_2)
        result_image_2 = cv2.cvtColor(result_image_2, cv2.COLOR_RGB2BGR) 
        st.image(result_image_2,caption="Detected Potholes",use_column_width=True)
