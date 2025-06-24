import streamlit as st
from ultralytics import YOLO
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import base64
import numpy as np

model=YOLO('backgroundRemover\model.pt')

st.set_page_config(layout="wide")
st.title('Background Remover')
st.header('Upload an image to remove background')

file = st.file_uploader('Upload image', type=['jpeg', 'jpg', 'png'])
col01, col02 = st.columns(2)

if file is not None:
    image = Image.open(file).convert('RGB')
    
    col01.image(image, caption="Original Image", use_container_width=True)
    
    if col01.button("Run YOLO Detection", type="primary", use_container_width=True):

        image=np.array(image)
        results = model(image,device='cpu')

        result = results[0]

        if result.masks is None:
            st.warning("No segmentation mask found.")
        else:
            masks = result.masks.data.cpu().numpy()  
            combined_mask = np.any(masks, axis=0).astype(np.uint8)  

            combined_mask = cv2.resize(combined_mask, (image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)

            alpha_channel = (combined_mask * 255).astype(np.uint8)
            rgba_image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
            rgba_image[:, :, 3] = alpha_channel  

            col02.image(rgba_image, caption="Image with Background Removed", use_container_width=True)

            result_pil = Image.fromarray(rgba_image)
            col02.download_button(
                label="Download Transparent PNG",
                data=result_pil.tobytes(),
                file_name="no_bg_image.png",
                mime="image/png",
                use_container_width=True
            )
