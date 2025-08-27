# AI Log Analysis

This project provides tools to analyze error logs using AI models. It includes two main scripts:

- **analyze_logs.py**: Sends log entries to OpenAI for detailed analysis and explanation.
- **langchain_analyzer.py**: Uses LangChain and Ollama (with the `phi3` model) to generate a plain-English explanation and a concise summary of error logs.

## Features

- **AI-powered log explanation**: Get thorough, plain-English explanations of error logs.
- **Summarization**: Automatically condense explanations into concise summaries.
- **Flexible LLM support**: Use either OpenAI or local Ollama models.

## Requirements

- Python 3.13+
- [LangChain](https://github.com/langchain-ai/langchain)
- [Ollama](https://ollama.com/) (for local LLM, e.g., `phi3`)
- OpenAI API key (for `analyze_logs.py`)
- Other dependencies as listed in `ai_venv/Lib/site-packages/`

## Setup

1. **Clone the repository** and navigate to the project folder.
2. **(Optional) Create and activate a virtual environment:**
   ```sh
   python -m venv ai_venv
   ai_venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
   *(You may need to manually create `requirements.txt` based on your environment.)*

4. **For Ollama-based analysis:**
   - Install and run [Ollama](https://ollama.com/download).
   - Pull the `phi3` model:
     ```sh
     ollama pull phi3
     ```

5. **For OpenAI-based analysis:**
   - Set your OpenAI API key as an environment variable:
     ```sh
     set OPENAI_API_KEY=your-key-here
     ```

## Usage

### Analyze logs with OpenAI

```sh
python analyze_logs.py sample.log
```

### Summarize logs with LangChain & Ollama

```sh
python langchain_analyzer.py
```

## File Structure

- `analyze_logs.py` — OpenAI-based log analysis.
- `langchain_analyzer.py` — LangChain/Ollama-based explanation and summarization.
- `sample.log` — Example log file.
- `requirements.txt` -Python dependencies

## Example Output

```
Executing the LangChain Sequential Chain...

==================================================
Original Log:
DatabaseConnectionError: Failed to connect to PostgreSQL database on host 127.0.0.1.

Full Explanation (from Step 1):
[AI-generated explanation here]

Concise Summary (from Step 2):
[AI-generated summary here]
==================================================
```
