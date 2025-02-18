import streamlit as st
import sys
import os
from constants import *
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from utils.chat import *
from utils.vector_embeddings import *
from utils.image_processing import *


st.title("Chatbot-for BAT")

col1, col2 = st.columns(2)
with col1:
    img1 = resize_image("images/CMSLogo_purple1.png", target_height = 200)
    st.image(img1, use_container_width = True)
with col2:
    img2 = resize_image("images/BAT.png", target_height = 200)
    st.image(img2, use_container_width = True)

st.markdown('''
            This is the home page.\n
            There are two pages with two versions for - BAT\n
            **Page 1:** BAT using OpenAI Embeddings & LLM.\n
            **Page 2:** BAT using Gemini & basic prompt template framework.
''')

   
    
