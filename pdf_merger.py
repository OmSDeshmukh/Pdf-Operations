import PyPDF2
import os

pdf_files = []

def Merge_pdfs(pdf_files):
    # To merge pdf inside of a directory
    merger = PyPDF2.PdfMerger()

    # To merge all the files together
    for file in pdf_files:
        merger.append(file)
        print("Files Merged Successfully")
            
    merger.write("combined.pdf")
    merger.close()