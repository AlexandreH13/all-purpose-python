'''
Using PyMuPDF and pillow to read and process images from PDF.

Dependencies: PyMuPDF and pillow
'''
from itertools import count
import fitz
import PIL.Image
import io # To work with image data

pdf = fitz.open("example.pdf")
counter = 1
for i in range(len(pdf)): # number of pages
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_image = pdf.extract_image(image[0])
        print(base_image) # meta data of the image
        image_data = base_image["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_image['ext'] # image extension
        img.save(open(f"image{counter}.{extension}", "wb"))
        counter += 1
