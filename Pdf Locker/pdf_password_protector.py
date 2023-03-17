import streamlit as st
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

st.set_page_config(page_title="PDF Password Protector")

st.title("PDF Password Protector")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
password = st.text_input("Set a password for the PDF")

if uploaded_file is not None and password != "":
    # Read the uploaded file
    pdf_reader = PdfFileReader(uploaded_file)

    # Create a new output PDF
    output = PdfFileWriter()

    # Add each page from the original PDF to the output PDF
    for page in range(pdf_reader.getNumPages()):
        output.add_page(pdf_reader.getPage(page))

    # Encrypt the output PDF with the given password
    output.encrypt(password)

    # Save the password-protected PDF to a temporary file
    with open("temp_protected.pdf", "wb") as file:
        output.write(file)

    # Display a download button to download the protected PDF
    with open("temp_protected.pdf", "rb") as file:
        st.download_button(
            label="Download Password-Protected PDF",
            data=file,
            file_name="protected.pdf",
        )
else:
    st.warning("Please upload a PDF file and set a password.")
