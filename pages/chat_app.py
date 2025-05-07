import streamlit as st
import sys
import os
import warnings
warnings.simplefilter("ignore", ResourceWarning)
import asyncio
import logging
import uuid
from datetime import datetime
from streamlit.web.server.websocket_headers import _get_websocket_headers
from traceloop.sdk import Traceloop
import json
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from utils.chat import qa_chat_with_prompt, stream_data
from utils.image_processing import display_images
from utils.files_processing import load_dict_from_json
from config import BAT_DATA, DEFAULT_QUERY, DEFAULT_FINAL_RESPONSE, ERROR_MESSAGE, BAT_LOGO_PATH
from logging_config import get_logger

logger = get_logger(__name__)

st.set_page_config(
    page_title="BAT chatbot",
    page_icon=BAT_LOGO_PATH,
    layout="wide",
    initial_sidebar_state="collapsed",
)


display_images()


if "bat_data" not in st.session_state:
    bat_data = load_dict_from_json(BAT_DATA)
    st.session_state["bat_data"] = bat_data

    
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []



if "chat_container" not in st.session_state:
    st.session_state.chat_container = st.container()

if "messages" not in st.session_state.keys():
    if "session_id" not in st.session_state.keys():
        session_id = "uuid-" + str(uuid.uuid4())

        logging.info(json.dumps({"_type": "set_session_id", "session_id": session_id}))
        Traceloop.set_association_properties({"session_id": session_id})
        st.session_state["session_id"] = session_id

        st.session_state["chat_history"] = [
            {"role": "user", "message": DEFAULT_QUERY},
            {"role": "assistant", "message": DEFAULT_FINAL_RESPONSE},
        ]

    #TODO: _get_websocket_headers is deprecated. Replace it with st.context.headers but even this is not JSON serializable so find a solution.
    # headers = _get_websocket_headers()
    # logging.info(
    #     json.dumps(
    #         {
    #             "_type": "set_headers",
    #             "headers": headers,
    #             "session_id": st.session_state.get("session_id", "NULL_SESS"),
    #         }
    #     )
    # )

if query:= st.chat_input("Ask a question"):
    st.session_state["chat_history"].append({
        "role": "user", 
        "message": query, 
    })

for chat in st.session_state["chat_history"]:
    with st.chat_message(chat["role"]):
        st.write(chat["message"])

if st.session_state["chat_history"][-1]["role"] != "assistant":  
    try:
        response = qa_chat_with_prompt(text = st.session_state["bat_data"], query = query)
        answer = response["answer"]
        source = response["source"]
        full_response = f"\n{answer}\n\n**Source:** {source}"
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                st.write_stream(stream_data(full_response))
                st.session_state["chat_history"].append({
                    "role": "assistant", 
                    "message": full_response, 
                })
        
    except Exception as e:
        logging.error(e)
        st.session_state["chat_history"].append({
            "role": "assistant",
            "message": ERROR_MESSAGE,
        })
        st.chat_message("assistant").write_stream(stream_data(ERROR_MESSAGE))