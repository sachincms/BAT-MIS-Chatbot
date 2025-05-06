from typing import List, Tuple
from typing import List
import os
import pandas as pd
import json
from pypdf import PdfReader
from datetime import datetime
from dotenv import load_dotenv

# Removed the old code
# In the chat_app we will use the bat.json file rather than bat_pdf_text.txt file

######################################## PDF to JSON #################################################
def convert_pdf_into_json(folder_path: str) -> dict:
  '''
  This function converts all pdf data into text string with pdf name as key and text as values
  Args:
    folder path containing all pdfs
  Returns:
    dict containing pdf name as key and text as values
  '''
  final_dict = {}
  pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

  for pdf_file in pdf_files:
    print(f"Currently working on {pdf_file}")
    text = ""
    pdf_path = os.path.join(folder_path, pdf_file)
    reader = PdfReader(pdf_path)

    for page in reader.pages:
      text += page.extract_text()

    final_dict[pdf_file] = text

  return final_dict


######################################## JSON processing #################################################

def custom_serializer(obj):
    """
    Serialize non-JSON serializable objects, such as datetime.
    Args:
        obj (any): The object to serialize.
    Returns:
        str: An ISO 8601 formatted string if the object is a datetime instance.
    Raises:
        TypeError: If the object type is not supported for serialization.
    """
    if isinstance(obj, datetime):
      return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not serializable")



def save_dict_to_json(input_dict: dict, file_path: str):
  '''
  This function saves the dictionary to JSON file
  Args:
    input dictionary, file path
  Returns:
    None
  '''
  with open(file_path, "w") as f:
    json.dump(input_dict, f, default=custom_serializer)



def load_dict_from_json(file_path: str) -> dict:
  '''
  This function loads the dictionary from json file
  Args:
    file path
  Returns:
    dictionary
  '''
  with open(file_path, "r") as f:
    loaded_dict  = json.load(f)
  return loaded_dict











