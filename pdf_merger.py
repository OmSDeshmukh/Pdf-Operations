import PyPDF2
import os

pdf_files = []

def Merge_pdfs(pdf_files):
    # To merge pdf inside of a directory
    merger = PyPDF2.PdfMerger()
    file_path = "files/combined.pdf"

    # To merge all the files together
    for file in pdf_files:
        merger.append(file)
        print("Files Merged Successfully")
            
    merger.write(file_path)
    merger.close()
    
    with open(file_path, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    return PDFbyte