# Importing necessary modules
from langchain_community.document_loaders import WebBaseLoader

# Function to extract text from URLs
def get_website_text(URLS):
    # Initializing WebBaseLoader with the provided URLs
    loader = WebBaseLoader(URLS)
       
    # Loading data from the URLs
    data = loader.load()   
    
    return data