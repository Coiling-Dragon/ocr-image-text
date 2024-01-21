from PIL import Image
import pytesseract
import os

# Define paths and tesseract command
images_dir = 'images'
text_dir = 'text'
output_file = 'output.txt'
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set tesseract command
pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

# Get list of all files in images directory
image_files = os.listdir(images_dir)

# Open the output file
with open(os.path.join(text_dir, output_file), 'a') as f:
    for image_file in image_files:
        # Open the image file
        image = Image.open(os.path.join(images_dir, image_file))
        # Use pytesseract to convert image to string
        text = pytesseract.image_to_string(image)
        # Write the image name as a header
        f.write(f'------= {image_file} =------\n')
        # Write the text
        f.write(text + '\n')