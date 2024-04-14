# Import necessary libraries
import os 
import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from utils import load_config


# Load configuration variables
config=load_config()
# Load environment variables from .env file
load_dotenv()
# Configure the GenerativeAI API with the Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# Initialize the Generative Model
model = genai.GenerativeModel(config['image_model']['model'])


# Function to process the uploaded image file
def get_image_text(upload_file,user_query):
    if upload_file is not None:
        # Read the file as bytes
        bytes_data = upload_file.getvalue()
        # Create a dictionary representing the image data
        image_parts = [
            {
                "mime_type": upload_file.type,
                "data": bytes_data
            }
        ] 
                
        input_prompt = """
        You are a wonderful assistant who has an excellent understanding of images and can describe them perfectly. A picture will be uploaded, and you will have to answer any questions based on the image. After that, you will need to give a detailed explanation.
        """

        response = model.generate_content([input_prompt, image_parts[0], user_query])

        return response.text