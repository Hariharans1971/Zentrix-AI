# Zentrix AI — LLM Chatbot

A Python chatbot project that experiments with a conversational interface using Streamlit and the Groq API. It is a learning project for API integration and LLM-powered responses.

## Features

- Chat interface built with Streamlit
- Optional responses through the Groq API
- Configurable model/provider integration
- Local development workflow

## Stack

Python · Streamlit · Groq API · LLMs

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Hariharans1971/Zentrix-AI.git
   cd Zentrix-AI
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Install dependencies from the repository's requirements file, if present:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Configure your Groq API key locally, using the variable name expected by the application. Never commit the key.

5. Run the Streamlit entry point shown in the source:

   ```bash
   streamlit run app.py
   ```

Check the repository's actual entry-point and dependency files before running; this README does not imply a hosted deployment.

## Security

- Keep API keys in environment variables or a local ignored `.env` file.
- Do not commit credentials, private prompts, or personal data.
- LLM output can be incorrect; verify important answers.
- Review provider pricing, rate limits, and current model availability.

## Roadmap

- Add a documented dependency lock or tested version ranges.
- Add tests for API failures and empty/invalid input.
- Add a clear setup example and sanitized screenshots.
- Document supported model IDs and actual response behavior.

## Author

Hariharan S. — B.Tech Computer Science and Engineering (AI & ML), 2026

[GitHub](https://github.com/Hariharans1971) · [LinkedIn](https://www.linkedin.com/in/hari-haran-b5aa50272/)
