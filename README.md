# Text-Detection-and-Extraction-using-OpenCV-ad-OCR
This project illustrates the process of detecting and extracting text from photos using Tesseract-OCR and OpenCV. Images are processed using OpenCV for tasks including contour detection, thresholding, and grayscale conversion. After processing, text is identified and extracted from the image using Tesseract-OCR. A file containing the extracted text is saved for later use.
# About
This project detects and extracts text from photos using Tesseract-OCR and OpenCV. After identifying text sections in photos, it extracts the text and saves it to a file. This program is helpful for effectively extracting information from photos and scanning printed documents.
# Required Installations
Before running the program, you need to install the following packages:
## Installation

To install the necessary packages, run the following commands:

```bash
pip install opencv-python
pip install pytesseract
```
# Steps to Run the Program
# 1.Install Required Packages:
```bash
pip install opencv-python pytesseract
```
# 2.Download and Install Tesseract-OCR:
Download Tesseract-OCR from this link and install it. Note the installation path (e.g., C:\Program Files\Tesseract-OCR\tesseract.exe).
# 3.Update the Tesseract Path in the Script:
Open the script and update the Tesseract-OCR path:
```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
# 4.Run the Program:
Execute the script:
```bash
python text_detection_extraction.py
```
# 5.Enter the Image Path:
When prompted, enter the path to the image you want to process. Ensure the path is correct and properly formatted.
# 6.View the Output:
The recognized text will be saved in the recognized.txt file in the same directory.
