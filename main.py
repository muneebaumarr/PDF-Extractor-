import PyPDF2
import streamlit as st



def extract_from_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text +=page_text

    return text

st.title("Welcome to PDF Extractor 📃")
option = st.radio("Select an option to Upload Pdf:" , ("Upload file", "Exit"))

if option == "Upload file":
    uploaded_file = st.file_uploader("Upload Your Pdf" , type=["pdf"])
    if uploaded_file is not None:
        st.success("File Uploaded Successfully!")
        text = extract_from_pdf(uploaded_file)
        st.subheader("📄 Extracted Text:")
        st.text_area("Text content", text, height=300)
        st.download_button(
            label="📥 Download Text File",
            data=text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
if option == "Exit":
    st.success("Good Bye! You Have Exited")



