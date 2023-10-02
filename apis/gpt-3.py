import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("GPT3_API_KEY")

gpt_prompt = "XXX"

def get_ai_gerneated_fact(gpt_prompt):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )

    fact = response['choices'][0]['text']
    return fact

print(get_ai_gerneated_fact(gpt_prompt=gpt_prompt))

