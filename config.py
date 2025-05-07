import os
from dotenv import load_dotenv

load_dotenv()

# EMBEDDING_MODEL = "text-embedding-3-small"
# MODEL_NAME = "gpt-3.5-turbo"
EMBED_DIMENSION = 512
CHUNK_SIZE = 1024
CHUNK_OVERLAP = 50
NODE_THRESHOLD = 0.5

current_file_path = os.getcwd()
LOGO_STYLE_HTML = os.path.join(current_file_path, "static",  "html", "logo_style.html")

BAT_LOGO_PATH = os.path.join(current_file_path, "static",  "images", "BAT.png")
CMS_LOGO_PATH = os.path.join(current_file_path, "static",  "images", "CMS.png")


GOOGLE_API_KEY_1 = os.getenv("GOOGLE_API_KEY_1")
GOOGLE_API_KEY_2 = os.getenv("GOOGLE_API_KEY_2")
GOOGLE_API_KEYS = [GOOGLE_API_KEY_1, GOOGLE_API_KEY_2]

LOGS_DIRECTORY = os.path.join(current_file_path, "logs")

MONGODB_URI = os.getenv("MONGODB_URI")
BAT_DATABASE = os.getenv("BAT_DATABASE")
USER_COLLECTION = os.getenv("USER_COLLECTION")
SITUATIONAL_REPORT_COLLECTION = os.getenv("SITUATIONAL_REPORT_COLLECTION")

BAT_DATA = os.path.join(current_file_path, "data", "bat.json")

INTRO_MESSAGE = """
India has over 172 million children at risk of harm, despite strong child protection laws. 
To tackle this, COF-KAWACH—a 10-year initiative by the British Asian Trust (BAT) and its partners—was launched in June 2022. 
The program works across Bihar, Uttar Pradesh, West Bengal, and Rajasthan, strengthening systems from grassroots to state levels to prevent child exploitation. 
By collaborating with local NGOs and government bodies, KAWACH aligns with India’s Mission Vatsalya to create safer childhoods.
"""
INTRO_MARKDOWN = """
<p>Ask anything about KAWACH:</p>
<ul>
<li>What are the key findings on child trafficking?</li>
<li>How does KAWACH support child protection laws?</li>
<li>Which organisations are implementing the program?</li>
<strong>Powered by real data & reports. Available anytime.</strong>
"""

DEFAULT_QUERY = "What is the KAWACH program about?"
DEFAULT_QUERY_RESPONSE = "The KAWACH program is a 10-year child protection initiative launched by the British Asian Trust (BAT) and other partners in June 2022. Its ambitious goal is to achieve a 30% reduction in child labor, child trafficking, child marriage, and commercial sexual exploitation of children, as well as a 50% reduction in online child sexual abuse and exploitation in high-prevalence states. The program aims to transform the child protection system by creating a comprehensive prevention model to establish a secure ecosystem, mitigate vulnerabilities, and bolster the prosecution of traffickers and exploiters. This involves building and strengthening systems from grassroots to state levels, preventing vulnerable children from cycles of exploitation, and leveraging data and evidence to guide decision-making, track progress, and refine strategies."
DEFAULT_RESPONSE_SOURCE = "About the program section of the Inception Report. Foreword section of the FINAL REPORT"
DEFAULT_FINAL_RESPONSE = f"\n{DEFAULT_QUERY_RESPONSE}\n\n**Source:** {DEFAULT_RESPONSE_SOURCE}"
ERROR_MESSAGE = "An error occurred while processing your request. Please try again later."