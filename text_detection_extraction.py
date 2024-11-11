## OCR Text Extraction Script

This Python script uses `opencv-python` and `pytesseract` to perform Optical Character Recognition (OCR) on an image specified by the user. The recognized text is saved to a file named `recognized.txt`.

```python
import cv2
import pytesseract

# Specify the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # Add the path of your computer

# Prompt the user to enter the image path
image_path = input("Please enter the path to the image: ").strip()

# Check if the image path contains both single and double quotes
if (image_path.startswith('"') and image_path.endswith('"')) or (image_path.startswith("'") and image_path.endswith("'")):
    # Remove the quotes
    image_path = image_path[1:-1]

# Replace backslashes with forward slashes
image_path = image_path.replace("\\", "/")

# Read the image from the specified path
img = cv2.imread(image_path)

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not read the image. Please check the path and try again.")
else:
    # Preprocessing the image starts

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray_image.jpg", gray)

    # Perform OTSU thresholding
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size for dilation
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Apply dilation on the thresholded image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

    # Find contours in the dilated image
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Create a copy of the original image to draw rectangles
    im2 = img.copy()

    # Open a text file to write the recognized text
    with open("recognized.txt", "w") as file:
        # Loop through the identified contours
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            # Draw a rectangle around the detected text area
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the text block for OCR
            cropped = im2[y:y + h, x:x + w]

            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)

            # Write the recognized text to the file
            file.write(text + "\n")

    print("Text extraction complete. Recognized text has been saved to 'recognized.txt'.")
  ```
