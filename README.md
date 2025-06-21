# Product-Authenticity-Checker
# 🛡️ Reviewing Genuine (or) fack products

A smart AI-powered tool that verifies the authenticity of products using **image analysis**, **QR scanning**. It combines **Google Gemini AI** with **UPCitemDB API** to cross-check product legitimacy.

---

## 🚀 Features

- ✅ Upload product images for AI-based counterfeit detection using **Gemini**
- ✅ Scan and extract **QR codes**
- ✅ Detect and read **barcodes** using OCR
- ✅ Cross-check barcode data using the **UPCitemDB API**
- ✅ Returns product name, brand, category, and authenticity confidence

---

## 🧠 Tech Stack

- [Streamlit](https://streamlit.io/) for UI  
- [Google Gemini API](https://ai.google.dev/) for image-based AI analysis  
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for barcode text extraction  
- [UPCitemDB](https://www.upcitemdb.com/) for product data lookup  
- [OpenCV](https://opencv.org/) for image preprocessing  

---

## 📦 Setup Instructions

1. Clone the repo**

git clone https://github.com/yourusername/product-authenticity-checker.git
cd product-authenticity-checker

2. Create virtual environment

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies

pip install -r requirements.txt

4. Configure environment

cp .env.example .env
# Fill in your Gemini and UPCitemDB API keys in the .env file

5. Run the app

streamlit run app.py

📜 License
MIT License.

![Screenshot 2025-06-21 160427](https://github.com/user-attachments/assets/44e8ff10-3622-427f-948c-e4f0848f279e)
![Screenshot 2025-06-21 160357](https://github.com/user-attachments/assets/7164e7aa-f8ba-4c95-8763-931e4131f274)
