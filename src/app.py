import os
import requests
import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(page_title="Flood Area Segmentation", layout="centered")


# Load U-Net model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("unet_model.keras")

model = load_model()

# Image preprocessing function
def preprocess_image(image):
    image = image.resize((256, 256))  # Resize to match model input size
    image = np.array(image) / 255.0   # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to generate segmentation mask
def predict_segmentation(image):
    preprocessed_image = preprocess_image(image)
    mask = model.predict(preprocessed_image)[0]  # Remove batch dimension

    # Convert mask to grayscale (remove last channel if exists)
    mask = np.squeeze(mask, axis=-1)  # Shape: (256, 256)

    # Convert mask to 0-255 range for visualization
    mask = (mask * 255).astype(np.uint8)  

    return mask

# Streamlit UI
st.title("Flood Area Segmentation using U-Net")
st.write("Upload an image, and the model will segment the flood-affected areas.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read image
    image = Image.open(uploaded_file)
    
    # Display original image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate segmentation mask
    if st.button("Segment Image"):
        mask = predict_segmentation(image)  # Generate mask
        mask_image = Image.fromarray(mask)  

        # Display segmentation result
        st.image(mask_image, caption="Segmented Image", use_column_width=True)

        # Download segmented mask
        st.download_button("Download Mask", mask_image.tobytes(), file_name="segmented_image.png", mime="image/png")
