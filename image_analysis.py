import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro-vision')

def analyze_image_with_gemini(image_path):
    img = Image.open(image_path)

    prompt = "Check if this product is genuine. Look for branding, packaging signs, serial numbers, QR codes, and suspicious details."

    response = model.generate_content(
        [prompt, img],
        generation_config={"max_output_tokens": 500}
    )

    return response.text
