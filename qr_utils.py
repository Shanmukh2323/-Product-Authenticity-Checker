from pyzbar.pyzbar import decode
from PIL import Image

def scan_qr_code(image_path):
    image = Image.open(image_path)
    decoded = decode(image)
    if decoded:
        return decoded[0].data.decode('utf-8')
    return "No QR code found."
