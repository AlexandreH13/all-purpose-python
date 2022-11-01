# install pdfminer.six
'''
Using pdfminer.six to extract text from PDF.

Dependencies: pdfminer.six
'''
import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("example.pdf") # Function to get all the text from the pdf
print(text)

pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}") # Get all text follow by one comma or one space
matches = pattern.findall(text)
print(matches)