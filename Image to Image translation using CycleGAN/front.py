import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import os
from models.networks import define_G

@st.cache_resource
def load_model(model_path):
    netG = define_G(input_nc=3, output_nc=3, ngf=64, netG='resnet_9blocks',norm='instance', init_type='normal', init_gain=0.02)
    netG.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    netG.eval()
    return netG

def transform_image(image):
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    return transform(image).unsqueeze(0)

def translate_image(model, image):
    with torch.no_grad():
        translated_image = model(image)
        translated_image = translated_image.squeeze().detach().cpu()
        translated_image = (translated_image + 1) / 2  
        return transforms.ToPILImage()(translated_image)

st.title("CycleGAN Image-to-Image Translation")
st.write("Upload an image to translate using the trained CycleGAN model")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Processing...")

    model_path = "C:/Users/Prajwal/OneDrive/Desktop/AIML-Projects/Image to Image translation using CycleGAN/checkpoints/cyclegan_model/latest_net_G_B.pth"
    if not os.path.exists(model_path):
        st.error("Model file not found! Please check the path.")
    else:
        model = load_model(model_path)
        transformed_image = transform_image(image)
        output_image = translate_image(model, transformed_image)
        st.image(output_image, caption="Translated Image", use_column_width=True)

