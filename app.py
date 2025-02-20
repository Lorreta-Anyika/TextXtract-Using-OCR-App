import pytesseract

# Set the Tesseract-OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from app import app

if __name__ == '__main__':
   app.run(debug=True)  # Optional: debug=True for easier troubleshooting

