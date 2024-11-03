import openai
from openai import OpenAI
client = OpenAI()

def get_completion(prompt, model="gpt-4o-mini"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content
response = get_completion("What is the capital of India?")
print(response)

response = get_completion("Take the letters in lollipop and reverse them")
print(response)