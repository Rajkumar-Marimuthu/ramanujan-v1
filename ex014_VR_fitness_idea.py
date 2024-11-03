from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "user",
      "content": "Brainstorm some ideas combining VR and fitness."
    }
  ],
  temperature=0.6,
  max_tokens=512,
  top_p=1
)
print(response.choices[0].message.content)