import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

pdf_path = "cfa-program2025L1V1.pdf"

extracted_text = extract_text_from_pdf(pdf_path)

with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
    output_file.write(extracted_text)
print("Text extracted and saved to 'extracted_text.txt'.")