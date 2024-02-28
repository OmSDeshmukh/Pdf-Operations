from docx2pdf import convert

def doc_to_pdf(doc_file_path):

    # Path to save the converted PDF file
    pdf_file_path = "path/to/save/converted/file.pdf"

    # Convert DOC to PDF
    convert(doc_file_path, pdf_file_path)
    return pdf_file_path