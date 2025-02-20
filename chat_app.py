import streamlit as st
import sys
import os
from constants import *
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from utils.chat import *
from utils.vector_embeddings import *
from utils.image_processing import *


st.title("Chatbot for KAWACH")

col1, col2 = st.columns(2)
with col1:
    img1 = resize_image("images/CMSLogo_purple1.png", target_height = 200)
    st.image(img1, use_container_width = True)
with col2:
    img2 = resize_image("images/BAT.png", target_height = 200)
    st.image(img2, use_container_width = True)

st.markdown('''
            India has over 172 million children at risk of harm, despite strong child protection laws. To tackle this, COF-KAWACH—a 10-year initiative by the British Asian Trust (BAT) and its partners—was launched in June 2022. The program works across Bihar, Uttar Pradesh, West Bengal, and Rajasthan, strengthening systems from grassroots to state levels to prevent child exploitation. By collaborating with local NGOs and government bodies, KAWACH aligns with India’s Mission Vatsalya to create safer childhoods.

            Ask anything about KAWACH:
            - What are the key findings on child trafficking?
            - How does KAWACH support child protection laws?
            - Which organisations are implementing the program?

            **Powered by real data & reports. Available anytime.**
''')

   
    
