# Text
import re
from pdfminer.high_level import extract_pages, extract_text
# Images
from itertools import count
import fitz
import PIL.Image
import io 
# Tables
import tabula
import pandas as pd

class ExtractFromPdf:
    """Implements functions to extract the main 3 types of
    data from PDF: Text, imagesa and tables.
    """

    def __init__(self, file_path) -> None:
        self.file_path = file_path

    def get_text(self) -> str:
        """Get the entire text from the PDF

        Returns:
            str: Text
        """
        text = extract_text(self.file_path)
        return text

    def get_text_re(self, re_pattern) -> list:
        """Return a text that matches the regex

        Args:
            re_pattern re.Pattern: regex pattern
        """

        pattern = re.compile(re_pattern)
        matches = pattern.findall(self.get_text())
        return matches

    def get_image(self) -> None:
        pdf = fitz.open(self.file_path)
        counter = 1
        for i in range(len(pdf)): # number of pages
            page = pdf[i]
            images = page.get_images()
            for image in images:
                base_image = pdf.extract_image(image[0]) # meta data of the image
                image_data = base_image["image"]
                img = PIL.Image.open(io.BytesIO(image_data))
                extension = base_image['ext'] # image extension
                img.save(open(f"image{counter}.{extension}", "wb"))
                counter += 1

    def get_tables(self) -> pd.DataFrame:
        tables = tabula.read_pdf(self.file_path, pages="all")
        df = tables[0]
        return df