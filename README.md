# LangChain Python Project

A small Python project experimenting with LangChain and OpenAI.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```powershell
pip install -r requirement.txt
```

3. Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key_here
MODEL_NAME=gpt-4o-mini
```

## Run

```powershell
python Chat\Chat.py
```

or

```powershell
python LLM\llm.py
```

## Notes

- Do not commit `.env` or any secret keys.
- If your account does not have access to a model, change `MODEL_NAME` to one you can use.

