# Import necessary libraries
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter,CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_community.embeddings import OllamaEmbeddings
from utils import load_config
from dotenv import load_dotenv


# Load configuration variables
config=load_config()
# Load environment variables 
load_dotenv()
# Configure the GenerativeAI API with the Google API key
api_key=os.getenv("GROQ_API_KEY")


# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config['textsplitter']['chunk_size'], 
        chunk_overlap=config['textsplitter']['chunk_overlap'],
        separators=config['textsplitter']['separators']
        )
    chunks = text_splitter.split_text(text)
    return chunks


# Function to create vector store from text chunks
def get_vector_store(text_chunks):
    embeddings = OllamaEmbeddings(model=config['embeddings']['model_name'])
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")


# Function to get base model and ollama model
def get_model():
    model = ChatGroq(model_name=config['model']['model_name'],
    temperature = config['model']['temperature'])
    return model


# Function to load conversational chain for question answering
def get_conversational_chain():
    prompt_template = """
    You are a wonderful assistant who has a great understanding of Vector documents and has advanced search functionalities.Please answer the question as clearly as possible from the provided context.
    If the answer is not available in the context, simply say, "Answer is not available in the Context"; please don't provide the wrong answer.\n\n
    Context:\n {context}?\n
    Question:\n{question}\n

    Answer:
    """
    model = get_model()
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain


# Function to handle user input and generate response
def user_input(user_question):
    embeddings = OllamaEmbeddings(model=config['embeddings']['model_name'])
    new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)
    chain = get_conversational_chain()   
    response = chain.invoke(
        {"input_documents":docs,
        "question": user_question},
        return_only_outputs=True
    )   
    return response["output_text"]
