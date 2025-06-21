import streamlit as st
from PIL import Image
import google.generativeai as genai
import io
import os
from dotenv import load_dotenv
import cv2
import numpy as np

# --- Load environment variables ---
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Load Gemini model ---
model = genai.GenerativeModel('models/gemini-1.5-flash')

# --- Streamlit UI setup ---
st.set_page_config(page_title="Product Authenticity Checker", layout="centered")
st.title("🛡️ Product Authenticity Checker")
st.markdown("""
Upload a product image to:
- 🔍 Check for embedded QR codes
- 🧠 Analyze visual authenticity using Google's Gemini AI
""")

uploaded_image = st.file_uploader("📷 Upload an image of the product", type=["jpg", "jpeg", "png"])

# --- QR scanner using OpenCV ---
def scan_qr_opencv(pil_img):
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    qr_detector = cv2.QRCodeDetector()
    data, points, _ = qr_detector.detectAndDecode(img)
    return data if data else None

# --- Process uploaded image ---
if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Step 1: QR Code Scanning
    qr_data = scan_qr_opencv(img)
    if qr_data:
        st.markdown("### 📲 QR Code Detected:")
        st.code(qr_data, language="text")
        # Optional: Validate or look up in your database here
    else:
        st.info("No QR code detected in the image.")

    # Step 2: Gemini Image Analysis
    if st.button("Check Authenticity"):
        with st.spinner("Analyzing image with Gemini AI..."):
            response = model.generate_content([
                "Analyze this product image and tell whether it looks like a genuine product or a counterfeit. Provide reasons for your answer."
                "and give the information about the product where it will be use."
                "At last give only one answer as genuine or fake",
                img
            ])
        st.success("Analysis complete!")
        st.markdown("### 🔍 Gemini Analysis:")
        st.write(response.text)
