# Optical Character Recognition (OCR) Web App  

## Overview  
This project is a simple OCR web application built using Flask and Tesseract-OCR. It allows users to upload images and extract text from them.  

## Prerequisites  
Before running the application, ensure you have the following installed:  
- Python (>=3.6)  
- Conda (Optional but recommended for virtual environment management)  
- Tesseract-OCR  

## Installation and Setup  

### Step 1: Clone the Repository  
Make a copy of the project by cloning the repository or downloading the files.  

### Step 2: Navigate to the Project Directory  
Open a terminal or command prompt and change the directory to the folder where `app.py` is located.  

```sh
cd path/to/project
```

### Step 3: Create a Virtual Environment  
Create a virtual environment using Conda:  

```sh
conda create --name ocr_app python=3.8
```

### Step 4: Activate the Environment  
Activate the virtual environment:  

```sh
conda activate ocr_app
```

### Step 5: Install Tesseract-OCR  
Download and install Tesseract-OCR from the following link:  
[Tesseract Installation](https://github.com/UB-Mannheim/tesseract/wiki)  

### Step 6: Configure Tesseract Path  
After installation, note the Tesseract path (default: `C:\Program Files\Tesseract-OCR\`) and update the `views.py` file:  

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Step 7: Install Dependencies  
Install the required dependencies using:  

```sh
python -m pip install -r requirements.txt
```

### Step 8: Run the Application  
Start the Flask application using:  

```sh
python app.py
```

### Step 9: Access the Web App  
Once the server is running, copy the provided URL (e.g., `http://127.0.0.1:5000/`) and paste it into a web browser to access the application.  

### Step 10: Test the OCR Functionality  
Use the `sample_data` folder to upload images and test text extraction.  

## Project Structure  
```
/project-folder
│── app.py
│── views.py
│── requirements.txt
│── static/
│   ├── uploads/
│   ├── images/
│── templates/
│   ├── index.html
│── sample_data/
```

## Features  
- Upload images for OCR processing  
- Extract text using Tesseract-OCR  
- Display extracted text in the web interface  

## Author  
**Anyika Uchechukwu Lorreta** 

## License  
MIT License  
