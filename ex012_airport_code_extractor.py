from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a text, and your task is to extract the airport codes from it."
    },
    {
      "role": "user",
      "content": "I want to fly from Orlando to Boston"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)