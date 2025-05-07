import streamlit as st
from utils.generate_sitrep import generate_situational_report
from utils.files_processing import load_dict_from_json
from utils.sitrep_db import check_sitrep_exists, store_sitrep
from utils.chat import stream_data
from config import BAT_DATA


st.set_page_config(page_title = "Situational Reports", layout = "wide")


json_data = load_dict_from_json(BAT_DATA)

select_pdf = st.selectbox("Select PDF", options = json_data.keys(), index = None)


if select_pdf:
    existing_sitrep = check_sitrep_exists(pdf_name = select_pdf)

    if existing_sitrep:
        sitrep = existing_sitrep["situational_report"]
        st.success("Loading existing situational report from database")
        st.write_stream(stream_data(sitrep))

    else:
        text = json_data[select_pdf]
        with st.spinner(f"Generating situational report for: {select_pdf}..."):
            sitrep = generate_situational_report(text = text)
            if sitrep:
                st.write_stream(stream_data(sitrep))
                store_sitrep(
                    pdf_name = select_pdf,
                    situational_report = sitrep
                )
