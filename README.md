# CareerOps Agent 🚀

A powerful AI agent that helps you apply for jobs by scraping job descriptions, analyzing your resume, and generating tailored cover letters.

Built with **Python**, **LangChain**, **Google Gemini**, and **Streamlit**.

## Features

- **Job Scraping**: Automatically extracts job descriptions from URLs.
- **Resume Analysis**: Uses RAG (Retrieval Augmented Generation) to understand your skills and experience from your resume.
- **Cover Letter Generation**: Writes professional, tailored cover letters using Google's Gemini-2.0-Flash model.
- **User Interface**: Simple and clean UI built with Streamlit.

## Tech Stack

- **LLM**: Google Gemini (gemini-2.0-flash)
- **Embeddings**: Google Gemini (text-embedding-004)
- **Framework**: LangChain
- **Vector Store**: FAISS
- **UI**: Streamlit

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd career-ops-agent
    ```

2.  **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    - Create a `.env` file in the root directory.
    - Add your Google API Key (Get one [here](https://aistudio.google.com/app/apikey)):
      ```
      GOOGLE_API_KEY=your_api_key_here
      ```

## Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

1.  Paste the **Job Description URL**.
2.  Upload your **Resume (PDF)**.
3.  Click **Generate Cover Letter**.

## License

MIT
