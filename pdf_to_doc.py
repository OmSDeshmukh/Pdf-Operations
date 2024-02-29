from pdf2docx import Converter

def pdf_to_doc(file):
    doc_file_path = "files/converted_to_doc.docx"
    # for file in pdf_files:
    # print(file)
    cv = Converter(file)
    cv.convert(doc_file_path)      # all pages by default
    cv.close()
    with open(doc_file_path, "rb") as docx_file:
        docx_bytes = docx_file.read()
    return docx_bytes