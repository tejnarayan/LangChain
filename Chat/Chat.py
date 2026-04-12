import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
	raise SystemExit(
		"Missing OPENAI_API_KEY. Put your key in .env (see .env.example) or set it in the current PowerShell session."
	)

model_name = os.getenv("MODEL_NAME", "gpt-4o-mini")
model = ChatOpenAI(model=model_name, temperature=1, max_completion_tokens=50)

result = model.invoke("suggest career advice for 13 year experience software engineer with .net and azure experience")

print(result.content)