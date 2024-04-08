import time
import streamlit as st
from streamlit_option_menu import option_menu
from langchain_core.messages import AIMessage, HumanMessage
from chain import *
from src.chatbot import get_chatbot_response
from src.pdf import get_pdf_text

st.set_page_config(page_title="Groq Chat Interface", page_icon="🤖")

with st.sidebar:
    selected = option_menu('Groq Chat Interface',
                           ['ChatBot','Audio','Image','PDF','Website','YouTube','DataFrame','DataBase' ],
                           menu_icon='none', 
                           icons=['robot','music-note-list','images','filetype-pdf', 'browser-chrome','youtube','table','database'],
                           default_index=0
                           )

    def clear_cache():
        keys = list(st.session_state.keys())
        for key in keys:
            st.session_state.pop(key)
    st.button('New Chat', on_click=clear_cache)

if selected in ['ChatBot','Audio','Image','PDF','Website','YouTube','DataFrame','DataBase']:
    title_dict = {'ChatBot': 'ChatBot','Audio': 'Audio','Image': 'Image','PDF': 'PDF', 
    'Website': 'Website', 'YouTube': 'YouTube','DataFrame': 'DataFrame','DataBase': 'DataBase'}
    st.title(f":red[Interactive Assistant] - :blue[{title_dict[selected]}]")
    st.write(" Meet your Intelligent Bot - Chat effortlessly with instant solution to all queries")

    if selected == 'PDF':
        pdf_docs = st.file_uploader("Upload your PDF Files ", accept_multiple_files=True, type="pdf")
    elif selected == 'Website':
        URLS = st.text_input(" Enter URL Here")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [AIMessage(content="“Hello 👋   How may I assist you today?”")]
    
    for message in st.session_state.chat_history:
        role = "AI" if isinstance(message, AIMessage) else "Human"
        with st.chat_message(role):
            st.write(message.content)
    
    user_query = st.chat_input("Message ChatBot...")
    
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
            
        with st.chat_message("AI"):
            with st.spinner("Generating answer..."):
                st_time = time.time()
                if selected == 'ChatBot':
                    response = get_chatbot_response(user_query, st.session_state.chat_history)
                elif selected == 'PDF':
                    if pdf_docs:
                        raw_text = get_pdf_text(pdf_docs)
                        text_chunks = get_text_chunks(raw_text)
                        get_vector_store(text_chunks)          
                        response = user_input(user_query)
                    else:
                        response = "Please upload a PDF file first."
                else:
                    # Add handling for other selected options here
                    response = "This option is not yet implemented."
                    
                if response is not None:
                    st.write(response)
                    st.session_state.chat_history.append(AIMessage(content=response))
                    st.write('Response Time = ',(time.time()-st_time))
