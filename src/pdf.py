# Import the PdfReader class from PyPDF2 library
from PyPDF2 import PdfReader

# Define a function to extract text from PDF documents
def get_pdf_text(pdf_docs):
    # Initialize an empty string to store the extracted text
    text = ""
    
    # Iterate through each PDF document
    for pdf in pdf_docs:
        # Create a PdfReader object for the current PDF document
        pdf_reader = PdfReader(pdf)
        
        # Iterate through each page in the PDF document
        for page in pdf_reader.pages:
            # Extract text from the current page and append it to the text variable
            text += page.extract_text()
    
    # Return the combined text extracted from all PDF documents
    return text
