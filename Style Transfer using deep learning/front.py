import streamlit as st
import torchvision.models as models
from Preprocess_image import Process_Image

st.title("Neural Style Transfer App")

uploaded_content = st.file_uploader("Upload Content Image")
st.image(uploaded_content)
uploaded_style = st.file_uploader("Upload Style Image")
st.image(uploaded_style)

vgg = models.vgg19(pretrained=True).features.eval()  

if st.button("Style Transfer"):

    if uploaded_content and uploaded_style:
        content = Process_Image.load_image(uploaded_content)
        style = Process_Image.load_image(uploaded_style)
        result = Process_Image.train_nst(content, style, vgg)
        processed_image = Process_Image.show_image(result)
        st.image(processed_image, caption="Styled Image", use_column_width=True)
