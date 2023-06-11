import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.organization = os.getenv('OPENAI_ORG')
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.Model.list()

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hi can you help me with some stuff",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
)

print(response.choices[0].text)