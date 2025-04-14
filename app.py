import streamlit as st
import numpy as np
from PIL import Image

st.title("Smart Wafer Defect Classifier")
st.write("Upload an image of a wafer to classify if it's defective or normal.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

def mock_predict(img_array):
    # Mock logic for demonstration
    return "Defective" if np.mean(img_array) < 128 else "Normal"

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L").resize((128, 128))
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    image_array = np.array(image)
    prediction = mock_predict(image_array)
    
    st.subheader("Prediction:")
    st.write(f"The wafer is **{prediction}**")
