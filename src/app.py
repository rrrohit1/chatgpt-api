# !pip install openai

import openai
import os

from dotenv import load_dotenv, find_dotEnv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model, 
    messages=messages,
    temperature=0 # amount of randomness in 
  )
  return response.choices[0].message["content"]

def main():
  get_completion("Summarize the text", "gpt-3.5-turbo")

if __name__ == "__main__":
  main()
