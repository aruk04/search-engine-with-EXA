# Search Engine

A simple search engine interface using the Exa API to perform intelligent searches.

- Building a custom search with an API that has LLM capabilities
- Accessing LLM’s is difficult due to large training time and high cost
- APIs are used to tackle this issue - it serves as a tool to perform NLP tasks - includes text generation, summarization, or even translation.

# What is EXA?

Exa (previously known as Metaphor) - API capable of retrieving the best information on the web - semantic searches are possible to retrieve high quality information.

Google - relies on keyword searches 
Exa understands the user’s input and the available content on the internet.

Exa uses LLMs as a core component - it has been trained extensively to understand human language.

Example implementation:

from exa_py import Exa

exa = Exa('YOUR_KEY_HERE')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()


Exa provides numerous filters for a search query. A couple of examples are listed below:
- highlights - Text snippets the LLM identifies as most relevant from each page
- numResults - the number of results you want to be returned
- include_domains - a list of domains that you want to be included in the search results
- start_published_date / end_published_date - Dates to restrict the results to content published in a certain time-range


## Prerequisites

- Python 3.x
- An Exa API key (get one from [Exa's website](https://exa.ai))

## Installation

1. Clone this repository or download the files
2. Install the required Python packages:

```bash
pip install python-dotenv exa-py
```

## Configuration

1. Create a `.env` file in the project root (or set environment variables directly)
2. Add your Exa API key to the `.env` file:

```
EXA_API_KEY=your_api_key_here
```

Alternatively, you can set the environment variable directly:

Windows (CMD):

```cmd
set EXA_API_KEY=your_api_key_here
```

Windows (PowerShell):

```powershell
$env:EXA_API_KEY = "your_api_key_here"
```

For permanent setup (Windows):

```cmd
setx EXA_API_KEY "your_api_key_here"
```

Note: After using `setx`, you'll need to open a new terminal window for the change to take effect.

## Usage

Run the search engine:

```bash
python main.py
```

The program will:

1. Prompt you to enter your search query
2. Use the Exa API to perform the search
3. Display the results

Example:

```
Search here: Best Chicago cold brew
[Search results will appear here...]
```

## Files

- `main.py` - The main search engine script
- `.env` - Environment configuration file (create this with your API key)

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key secure and don't share it
- Consider adding `.env` to your `.gitignore` file

## Error Handling

The script will show helpful error messages if:

- The API key is not set
- There are connection issues
- The search query fails


