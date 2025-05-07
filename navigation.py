import streamlit as st

pages = [
    st.Page("chat_app.py", title = "Chatbot"),
    st.Page("situational_reports.py", title = "Situational Reports"),
    st.Page("manage_users.py", title = "User Management")
]

pg = st.navigation(pages)
pg.run()