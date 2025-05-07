from config import SITUATIONAL_REPORT_COLLECTION
from handlers.MongoDBHandler import MongoDBHandler
from logging_config import get_logger

logger = get_logger(__name__)


mongodb_handler = MongoDBHandler(SITUATIONAL_REPORT_COLLECTION)


def check_sitrep_exists(pdf_name: str) -> dict:
    """
    Check if a situational report already exists in the MongoDB collection 
    based on the provided identifiers.
    Args:
        pdf_name (str, optional): Name of the PDF file (required for Progress Report Partners).
    Returns:
        dict or None: The first matching case story document if found, otherwise None.
    """
    query = {
            "pdf_name": pdf_name
        }

    results = mongodb_handler.read_data(query)
    if results:
        return results[0]
    return None


def store_sitrep(pdf_name: str = None, situational_report:str = None):
    """
    Store a situational report in the MongoDB collection if it does not already exist.
    Arguments:
        pdf_name (str, optional): Name of the PDF file (required for Progress Report Partners).
    Returns:
        None
    """
    data = {
            'pdf_name': pdf_name,
            'situational_report': situational_report
        }
    query = {'pdf_name': pdf_name}

    existing_sitrep = check_sitrep_exists(query)
    if not existing_sitrep:
        mongodb_handler.insert_data(data)
