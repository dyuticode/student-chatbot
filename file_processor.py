from PyPDF2 import PdfReader
from docx import Document
import pandas as pd

def process_file(uploaded_file):

    text = ""

    if uploaded_file is None:

        return text

    if uploaded_file.type == "application/pdf":

        reader = PdfReader(uploaded_file)

        for page in reader.pages:

            content = page.extract_text()

            if content:

                text += content

    elif uploaded_file.name.endswith(".docx"):

        doc = Document(uploaded_file)

        for para in doc.paragraphs:

            text += para.text + "\n"

    elif uploaded_file.name.endswith(
        (".xlsx", ".xls")
    ):

        df = pd.read_excel(uploaded_file)

        text += df.to_string()

    return text