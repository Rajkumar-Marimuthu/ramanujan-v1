from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a text, and your task is to create a numbered list of turn-by-turn directions from it."
    },
    {
      "role": "user",
      "content": "Go south on 95 until you hit Sunrise boulevard then take it east to us 1 and head south. Tom Jenkins bbq will be on the left after several miles."
    }
  ],
  temperature=0.3,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)