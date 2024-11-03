from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a product description and seed words, and your task is to generate product names."
    },
    {
      "role": "user",
      "content": "Product description: A home milkshake maker\n    Seed words: fast, healthy, compact."
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)