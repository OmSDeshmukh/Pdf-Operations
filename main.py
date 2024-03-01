import streamlit as st
from pdf_merger import Merge_pdfs
import os
from pdf_to_doc import pdf_to_doc
from doc_to_pdf import doc_to_pdf
# Get the directory of the current script
# script_directory = os.path.dirname(os.path.abspath(__file__))
# print(script_directory)
st.title("PDF Operations")

option = st.radio("Select an option:", ("Merge PDF files", "Convert PDF to DOC"))

if option == "Merge PDF files":
    st.title("Merge PDF files")
    uploaded_files = st.file_uploader("Choose files", type=['pdf'], accept_multiple_files=True)

    if st.button("Merge PDF files"):
        if uploaded_files:
            try:
                PDFbyte = Merge_pdfs(uploaded_files)
                st.success("PDFs merged successfully!")
                download_message = st.empty()
                st.download_button(
                    label="Click here to download PDF",
                    data=PDFbyte,
                    file_name="merged_pdf.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"Failed to merge PDFs: {str(e)}")
        else:
            st.warning("Please upload PDF files to merge.")

elif option == "Convert PDF to DOC":
    st.title("Convert PDF to DOC")
    uploaded_file = st.file_uploader("Upload PDF file", type=['pdf'], accept_multiple_files=False)

    if st.button("Convert PDF to DOC"):
        if uploaded_file:
            try:
                docx_bytes = pdf_to_doc(uploaded_file)
                st.success("PDF converted to DOC successfully!")
                st.download_button(
                    label="Click here to download the doc",
                    data=docx_bytes,
                    file_name="converted_to_doc.docx",
                    mime="docx"
                )
            except Exception as e:
                st.error(f"Failed to convert PDF to DOC: {str(e)}")
        else:
            st.warning("Please upload a PDF file to convert.")
            
            
# elif option == "Convert DOC to PDF":
#     st.title("Convert  DOC to PDF")
#     uploaded_file = st.file_uploader("Upload PDF file", type=['docx'], accept_multiple_files=False)

#     if st.button("Convert PDF to DOC"):
#         if uploaded_file:
#             try:
#                 docx_bytes = doc_to_pdf(uploaded_file)
#                 st.success("DOC converted to PDF successfully!")
#                 st.download_button(
#                     label="Click here to download the pdf",
#                     data=docx_bytes,
#                     file_name="converted_to_pdf.pdf",
#                     mime="docx"
#                 )
#             except Exception as e:
#                 st.error(f"Failed to convert DOC to PDF: {str(e)}")
#         else:
#             st.warning("Please upload a DOC file to convert.")