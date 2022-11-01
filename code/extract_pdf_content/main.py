from get_data import ExtractFromPdf

pdf_file = "example.pdf"

extract_data = ExtractFromPdf(pdf_file)

print(extract_data.get_text())