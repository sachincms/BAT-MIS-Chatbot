import llama_index
from llama_index.core import PromptTemplate
from llama_index.llms.gemini import Gemini
from llama_index.core.base.llms.types import ChatMessage
from config import GOOGLE_API_KEYS, GEMINI_MODEL_NAME
from utils.chat import switch_google_api_key
from requests.exceptions import HTTPError, ConnectionError, Timeout
from time import time
from typing import List
from logging_config import get_logger

logger = get_logger(__name__)

def convert_query_into_chat(text: str) -> List[llama_index.core.base.llms.types.ChatMessage]:
    '''
        This function converts the input text & query into chat message template
        Args:
            Input context text & query
        Returns:
            Chat Message template 
    '''
    prompt_template_str = (
        "You are a development impact writer. Based on the context below, generate a NEW situational report. "
        "Use a compelling, human-centered tone. Structure it with:\n"
        '''
        1. Title

        2. Case Reported- numbers total and key districts
        3. Any government schemes or department work on these case types and highlights of those

        '''

        "DO NOT copy any part of the example used earlier. Only use facts and ideas from the context.\n\n"
        "----------- CONTEXT -----------\n"
        "{context_str}\n"
        "----------- END CONTEXT -----------\n\n"
        "Start your situational report below:"
    )
    prompt = PromptTemplate(prompt_template_str)
    prompt_text = prompt.format(context_str=text)
    return [ChatMessage(role="user", content=prompt_text)]


def generate_situational_report(text: str) -> str:
    '''
    This function generates situational report
    Args:
      Input text 
    Returns:
      situational report
     '''
    message = convert_query_into_chat(text)

    current_index = 0
    while True:
        try:
            api_key = GOOGLE_API_KEYS[0]
            llm = Gemini(model = GEMINI_MODEL_NAME, api_key = api_key)
            response = llm.chat(message)
            try:
                return response.message.content.strip()
            except:
                return response.text.strip()
            
        except HTTPError as e:
            if e.response.status_code == 429:
                try:
                    current_index = switch_google_api_key(current_index)
                    time.sleep(2)
                except ValueError:
                    raise ValueError("All API keys are exhausted or invalid")
                
            elif e.response.status_code in [501, 502, 503, 504]:
                logger.error(f"Server error {e.response.status_code}: {e.response.text}")
                return  None
        
            elif e.response.status_code in [401, 401, 403, 404]:
                logger.error(f"Client error {e.response.status_code}: {e.response.text}")
                return  None
            else:
                raise e 
        
        except (ConnectionError, Timeout) as e:
            logger.error(f"Network error: {str(e)}")
            return  None
        
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            return  None
