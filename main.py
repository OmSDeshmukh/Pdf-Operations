import streamlit as st
from pdf_merger import Merge_pdfs
import os
from get_binary_file import get_binary_file_downloader_html

st.title("File Upload and Download Example")

uploaded_files = st.file_uploader("Choose files", type=['pdf'], accept_multiple_files=True)

if(st.button("Upload pdf files")):
    if uploaded_files is not None:
        st.write("Files uploaded successfully!")
        try:
            Merge_pdfs(uploaded_files)
        except:
            st.write("Could not merge PDF files")
            # return 
        st.write("PDF combined Successfully")
        
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "combined.pdf")
        
        with open(file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        download_message = st.empty()
        st.download_button(label = "Download combined pdf files", data = PDFbyte,file_name = file_path,on_click = lambda: download_message.write("Download Successful"))
    else:
        st.write("No file to merge!") 
# Terminal interface
# while True:
#     path = input("Enter the path of a PDF file (or type 'exit' to stop): ")
#     if path.lower() == 'exit':
#         break
#     elif os.path.isfile(path) and path.lower().endswith('.pdf'):
#         pdf_files.append(path)
#     else:
#         print("Invalid path or file is not a PDF.")

# if __name__ == "__main__":
#     main()
