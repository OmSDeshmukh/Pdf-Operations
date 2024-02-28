import streamlit as st
from pdf_merger import Merge_pdfs
import os
from get_binary_file import get_binary_file_downloader_html
from doc_to_pdf import doc_to_pdf

st.title("PDF Operations")

option = st.radio("Select an option:", ("Merge PDF files", "Convert PDF to DOC"))

if(option == "Merge PDF files"):
    st.title("Merge PDF files")
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
elif(option=="Convert PDF to DOC"):
    st.title("Convert PDF to DOC")
    uploaded_file = st.file_uploader("Upload doc files", type=['docx'])
    
    if st.button("Upload docx files"):
        if uploaded_file is not None:
            st.write("File uploaded successfully!")
            try:
                doc_to_pdf(uploaded_file)
                st.write("DOC converted to PDF successfully")
            except:
                st.write("Could not convert PDF to DOC")
                
            # File uploading to be done
            # cwd = os.getcwd()
            # file_path = os.path.join(cwd, "combined.pdf")
            
            # with open(file_path, "rb") as pdf_file:
            #     PDFbyte = pdf_file.read()

            # download_message = st.empty()
            # st.download_button(label = "Download combined pdf files", data = PDFbyte,file_name = file_path,on_click = lambda: download_message.write("Download Successful"))
        else:
            st.write("No file to convert!")