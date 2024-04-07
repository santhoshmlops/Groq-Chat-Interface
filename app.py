
import streamlit as st
from streamlit_option_menu import option_menu



st.set_page_config(page_title="Groq Chat Interface", page_icon="🤖")

with st.sidebar:
    selected = option_menu('Groq Chat Interface',
                           ['ChatBot','Audio','Image','PDF','Website','YouTube','DataFrame','DataBase' ],
                           menu_icon='none', 
                           icons=['robot','music-note-list','images','filetype-pdf', 'browser-chrome','youtube','table','database'],
                           default_index=0
                           )


if selected == 'ChatBot':
    st.title(":red[Chat Interface] - :blue[ChatBot]")

if selected == 'Audio':
    st.title(":red[Chat Interface] - :blue[Audio]")

if selected == 'Image':
    st.title(":red[Chat Interface] - :blue[Image]")

if selected == 'PDF':
    st.title(":red[Chat Interface] - :blue[PDF]")

if selected == 'Website':
    st.title(":red[Chat Interface] - :blue[Website]")

if selected == 'YouTube':
    st.title(":red[Chat Interface] - :blue[YouTube]")

if selected == 'DataFrame':
    st.title(":red[Chat Interface] - :blue[DataFrame]")

if selected == 'DataBase':
    st.title(":red[Chat Interface] - :blue[DataBase]")
    