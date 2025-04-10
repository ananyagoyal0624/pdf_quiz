import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # ✅ New import as per updated LangChain

# Load environment variables from .env file
load_dotenv()

class QaLlm():
    def __init__(self) -> None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found. Check your .env file or environment setup.")
        
        self.llm = ChatOpenAI(
            temperature=0,
            model_name="gpt-3.5-turbo",
            openai_api_key=api_key.strip()
        )

    def get_llm(self):
        return self.llm
