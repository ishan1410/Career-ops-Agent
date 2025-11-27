import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.tools import tool
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 1. Setup
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Error: GOOGLE_API_KEY not found in .env file.")

# Initialize Gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

# 2. Tool 1: Scraper
@tool
def scrape_job(url: str) -> str:
    """Scrapes the job description from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text and clean it up a bit
        text = soup.get_text(separator=' ', strip=True)
        return text[:5000] # Limit text length to avoid token limits
    except Exception as e:
        return f"Error scraping URL: {e}"

# 3. Tool 2: RAG (Resume)
def create_resume_retriever_tool(resume_text: str):
    try:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = text_splitter.split_text(resume_text)
        
        # Use Gemini Embeddings
        embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
        db = FAISS.from_texts(texts, embeddings)
        retriever = db.as_retriever()
        
        tool = create_retriever_tool(
            retriever,
            "search_resume",
            "Searches and returns excerpts from the user's resume."
        )
        return tool
    except Exception as e:
        print(f"Error creating resume tool: {e}")
        return None

def get_agent(resume_text: str):
    resume_tool = create_resume_retriever_tool(resume_text)
    tools = [scrape_job]
    if resume_tool:
        tools.append(resume_tool)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful career assistant."),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_openai_functions_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor

# 5. Execution
if __name__ == "__main__":
    # Load dummy resume for local testing
    try:
        with open("dummy_resume.txt", "r") as f:
            dummy_resume = f.read()
    except FileNotFoundError:
        dummy_resume = "Ishan is a software engineer."

    agent_executor = get_agent(dummy_resume)
    
    job_url = "https://boards.greenhouse.io/lyzr/jobs/12345"
    user_prompt = f"Scrape the job description from the URL {job_url}. Then, search my resume for matching skills. Finally, write a cover letter tailored to this job."
    
    print(f"Running agent with prompt: {user_prompt}")
    try:
        agent_executor.invoke({"input": user_prompt})
    except Exception as e:
        print(f"Execution failed: {e}")
