import streamlit as st
from pdf_merger import Merge_pdfs
import os
from get_binary_file import get_binary_file_downloader_html

st.title("File Upload and Download Example")

uploaded_files = st.file_uploader("Choose files", type=['pdf'], accept_multiple_files=True)

if uploaded_files is not None:
    st.write("Files uploaded successfully!")
    
    Merge_pdfs(uploaded_files)

st.text("Files combined Successfully")

if(st.btn("Download Combined File")):
    cwd = os.getcwd()
    file_path = os.path.join(cwd, "combined.pdf")
    with open(file_path, "rb") as f:
        file_content = f.read()
    st.markdown(get_binary_file_downloader_html(file_path, file_content), unsafe_allow_html=True)

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
