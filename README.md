# Search Engine

A simple search engine interface using the Exa API to perform intelligent searches.

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


