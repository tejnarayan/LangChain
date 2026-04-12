import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()


# Use a chat model. Override with env var MODEL_NAME if needed.
model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
llm = ChatOpenAI(model=model_name)

result = llm.invoke("Which is best LLM?")
print(result.content)
