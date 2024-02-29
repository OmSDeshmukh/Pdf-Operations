from docx2pdf import convert
import os
import tempfile

def doc_to_pdf(docx_file):
    temp_dir = tempfile.TemporaryDirectory()
    docx_file_path = os.path.join(temp_dir.name, docx_file.name)
    with open(docx_file_path, "wb") as f:
        f.write(docx_file.getbuffer())
        
    cwd = os.getcwd()
    pdf_file_path = os.path.join(cwd, "files", "converted_to_pdf.pdf")
                
    # Convert DOCX to PDF
    convert(docx_file_path, pdf_file_path)
    
    with open(pdf_file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    
    # Clean up temporary directory
    temp_dir.cleanup()
    
    return PDFbyte