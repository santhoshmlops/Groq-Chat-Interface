# Import necessary libraries
import time
import streamlit as st
from streamlit_option_menu import option_menu
from langchain_core.messages import AIMessage, HumanMessage
from chain import *
from src.chatbot import get_chatbot_response

# Set page configuration
st.set_page_config(page_title="Groq Chat Interface", page_icon="🤖")

# Sidebar menu options
with st.sidebar:
    # Dropdown menu for selecting chat interface options
    selected = option_menu('Groq Chat Interface',
                           ['ChatBot','Audio','Image','PDF','Website','YouTube','DataFrame','DataBase' ],
                           menu_icon='none', 
                           icons=['robot','music-note-list','images','filetype-pdf', 'browser-chrome','youtube','table','database'],
                           default_index=0
                           )
    
    # Function to clear chat history
    def clear_cache():
        keys = list(st.session_state.keys())
        for key in keys:
            st.session_state.pop(key)
    # Button to initiate a new chat session
    st.button('New Chat', on_click=clear_cache)

# Display selected chat interface title
if selected in ['ChatBot','Audio','Image','PDF','Website','YouTube','DataFrame','DataBase']:
    title_dict = {'ChatBot': 'ChatBot','Audio': 'Audio','Image': 'Image','PDF': 'PDF', 
    'Website': 'Website', 'YouTube': 'YouTube','DataFrame': 'DataFrame','DataBase': 'DataBase'}
    st.title(f":orange[Interactive Assistant] - :grey[{title_dict[selected]}]")
    st.write(" Meet your Intelligent Bot - Chat effortlessly with instant solution to all queries")

    # Creating file uploader for specific interfaces
    if selected in ['Audio','Image','PDF','DataFrame','DataBase']:
        file_upload = st.file_uploader("Upload your Files ", accept_multiple_files=True)
    
    # Creating text input for URL
    elif selected in ['Website','YouTube']:
        url = st.text_input(" Enter URL Here")


    # Initialize chat history if not present
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [AIMessage(content="“Hello 👋   How may I assist you today?”")]
    
    # Iterate through chat history and display messages
    for message in st.session_state.chat_history:
        role = "AI" if isinstance(message, AIMessage) else "Human"
        with st.chat_message(role):
            st.write(message.content)
    
    # Input field for user query
    user_query = st.chat_input("Message Groq Chat-Interface...")
    
    # Process user query and generate response
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
            
        with st.chat_message("AI"):
            with st.spinner("Generating answer..."):
                st_time = time.time()

                # Process different chat interface options
                if selected == 'ChatBot':
                    response = get_chatbot_response(user_query, st.session_state.chat_history)
                
                elif selected == 'Audio':
                    pass
                
                elif selected == 'Image':
                    pass
                
                elif selected == 'PDF':
                    pass
                
                elif selected == 'Website':
                    pass
                
                elif selected == 'YouTube':
                    pass
                
                elif selected == 'DataFrame':
                    pass
                
                elif selected == 'DataBase':
                    pass
                
                else:
                    response = "This option is not yet implemented."
                    
                # Display response and calculate response time
                if response is not None:
                    st.write(response)
                    st.session_state.chat_history.append(AIMessage(content=response))
                    st.write('Response Time = ',(time.time()-st_time))
