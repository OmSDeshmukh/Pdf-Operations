from pdf2docx import Converter
import tempfile 

def pdf_to_doc(file):
    with tempfile.NamedTemporaryFile(delete=False,suffix='.pdf') as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name
        
        if temp_file_path:
            cv = Converter(temp_file_path)
            cv.convert("files/converted_to_doc.docx")
            cv.close()
        
        with open("files/converted_to_doc.docx", "rb") as docx_file:
            docx_bytes = docx_file.read()
    return docx_bytes