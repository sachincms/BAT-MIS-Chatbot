import streamlit as st
from utils.generate_sitrep import generate_situational_report
from utils.files_processing import load_dict_from_json
from utils.sitrep_db import check_sitrep_exists, store_sitrep
from config import BAT_DATA


st.set_page_config(page_title = "Situational Reports", layout = "wide")

if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    st.error("Please log in first")
    st.stop()



json_data = load_dict_from_json(BAT_DATA)

select_pdf = st.selectbox("Select PDF", options = json_data.keys())


if select_pdf:
    existing_sitrep = check_sitrep_exists(pdf_name = select_pdf)

    if existing_sitrep:
        sitrep = existing_sitrep["case_story"]
        st.success("Loading existing situational report from database")
        st.write(sitrep)

    else:
        text = json_data[select_pdf]
        with st.spinner(f"Generating situational report for Partner: {select_pdf}..."):
            sitrep = generate_situational_report(text = text)
            if sitrep:
                st.write(sitrep)
                store_sitrep(
                    pdf_name = select_pdf,
                    situational_report = sitrep
                )

       



        
 
