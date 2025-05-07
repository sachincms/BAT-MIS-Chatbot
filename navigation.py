import streamlit as st
import os

pages = [
    st.Page(os.path.join("pages","chat_app.py"), title = "Chatbot"),
    st.Page(os.path.join("pages", "situational_reports.py"), title = "Situational Reports"),
]

pg = st.navigation(pages)
pg.run()