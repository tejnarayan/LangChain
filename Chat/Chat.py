from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1, max_completion_tokens=50)

result = model.invoke("suggest career advice for 13 year experience software engineer with .net and azure experience")

print(result.content)