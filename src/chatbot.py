# Import necessary libraries
import streamlit as st
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from chain import get_model
from utils import load_config

# Load configuration variables
config=load_config()

# Define function to get the response from the chatbot
def get_chatbot_response(user_query, chat_history):
    # Define a template for the chat prompt
    template = """
    You are a helpful assistant. Answer the following questions asked by the user in detail.
    Chat history: {chat_history}
    User question: {user_question}
    """
    
    # Create a ChatPromptTemplate object from the template
    prompt = ChatPromptTemplate.from_template(template)

    # Get the specified model
    model = get_model()

    # Define a chain of operations for the chatbot
    chain = prompt | model | StrOutputParser()
    
    # Stream the input to the chain and get the response
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query,
    })