from dotenv import load_dotenv
import os
import openai


load_dotenv()

client = openai.OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key=os.environ.get("CEREBRAS_API_KEY")
)

chat_completion = client.chat.completions.create(
  messages=[
  {"role": "user", "content": "Why is fast inference important?",}
],
  model="llama3.1-8b",
)

print(chat_completion)



