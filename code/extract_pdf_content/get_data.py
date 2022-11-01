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
        pass

    def get_tables(self) -> pd.DataFrame:
        pass