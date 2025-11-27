# CareerOps Agent

**CareerOps Agent** is an intelligent, AI-powered career assistant designed to streamline your job application process. By leveraging the power of **Google Gemini** and **LangChain**, this tool automatically analyzes job descriptions, cross-references them with your resume, and generates highly tailored, professional cover letters in seconds.

## Features

-   **Smart Job Scraping**: Automatically extracts and parses job descriptions from any given URL.
-   **Resume Analysis (RAG)**: Uses Retrieval-Augmented Generation to understand your specific skills, experiences, and achievements from your uploaded PDF resume.
-   **Tailored Content Generation**: Generates a unique cover letter that bridges the gap between your experience and the job requirements.
-   **Modern UI**: A clean, user-friendly interface built with Streamlit.
-   **Free Tier Compatible**: Optimized to run on Google Gemini's free tier (Gemini 2.0 Flash).

## Tech Stack

-   **Core Logic**: Python 3.11+
-   **LLM Engine**: Google Gemini (gemini-2.0-flash)
-   **Embeddings**: Google Gemini (text-embedding-004)
-   **Orchestration**: LangChain
-   **Vector Store**: FAISS (Facebook AI Similarity Search)
-   **Frontend**: Streamlit
-   **PDF Processing**: PyPDF

## Architecture

The application follows a modular agentic architecture:

1.  **Input**: User provides a Job URL and uploads a Resume (PDF).
2.  **Processing**:
    *   The **Scraper Tool** fetches the job description from the web.
    *   The **RAG Tool** chunks and embeds the resume into a vector store for semantic search.
3.  **Reasoning**: The **LangChain Agent** (powered by Gemini) plans the execution:
    *   It first scrapes the job to understand requirements.
    *   It then searches the resume for relevant matching skills.
    *   Finally, it synthesizes this information to write the cover letter.
4.  **Output**: The generated cover letter is displayed in the UI.

## Getting Started

### Prerequisites

-   Python 3.9 or higher
-   A Google Cloud API Key (Get it for free [here](https://aistudio.google.com/app/apikey))

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/ishan1410/Career-ops-Agent.git
    cd Career-ops-Agent
    ```

2.  **Set up Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**
    Create a `.env` file in the root directory and add your API key:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

### Running the Application

Start the Streamlit server:
```bash
streamlit run app.py
```
The application will open automatically in your default browser at `http://localhost:8501`.

## Project Structure

```text
career-ops-agent/
├── agent.py           # Core logic: Tools, LLM setup, and Agent definition
├── app.py             # Frontend: Streamlit UI and event handling
├── dummy_resume.txt   # Sample data for testing
├── list_models.py     # Utility script to check available Gemini models
├── requirements.txt   # Project dependencies
├── .env               # Environment variables (API Keys)
└── README.md          # Documentation
```

## Code Overview

### `agent.py`
This is the brain of the application.
-   **`scrape_job(url)`**: A custom LangChain tool that uses `requests` and `BeautifulSoup` to extract text from job postings.
-   **`create_resume_retriever_tool(resume_text)`**: Converts raw resume text into vector embeddings using `text-embedding-004` and stores them in a FAISS index. This allows the AI to "search" your resume.
-   **`get_agent(resume_text)`**: Assembles the tools and initializes the ReAct agent using `gemini-2.0-flash`.

### `app.py`
Handles the user interaction.
-   Accepts user input (URL string and PDF file).
-   Extracts text from the uploaded PDF using `pypdf`.
-   Calls `get_agent()` to initialize the backend.
-   Displays the final streaming response to the user.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
**Author**: Ishan Patel
