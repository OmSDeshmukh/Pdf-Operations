from docx2pdf import convert
import tempfile

import os

def doc_to_pdf(docx_file):
    with tempfile.NamedTemporaryFile(delete=False,suffix='.docx') as temp_file:
        temp_file.write(docx_file.read())
        temp_file_path = temp_file.name
        
        convert(temp_file_path,"files/conveted_to_pdf.pdf")
        with open("files/conveted_to_pdf.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
    return PDFbyte
