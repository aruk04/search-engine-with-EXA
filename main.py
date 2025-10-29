import os
from dotenv import load_dotenv
from exa_py import Exa

# Load environment variables from a .env file (if present)
load_dotenv()

# Read the EXA API key from the environment
exa_api_key = os.getenv("EXA_API_KEY")
if not exa_api_key:
    raise RuntimeError(
        "EXA_API_KEY is not set. Please set it in your environment or in a .env file at the project root."
    )

# Initialize the client
exa = Exa(exa_api_key)

# Prompt the user and run the search
query = input("Search here: ")

response = exa.search(
    'best pizza in Brooklyn',
    num_results=10,
    start_published_date='2023-05-01', 
    category='tweet', 
#     use_autoprompt=True,
)

# print(response)