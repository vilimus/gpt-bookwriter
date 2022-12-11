import requests
import re

class Book():
  def __init__(self, title, author=None):
    self.title = title
    self.author = author
    self.chapters = []

class Chapter():
  def __init__(self, title):
    self.title = title
    self.sections = []

class Section():
  def __init__(self, title):
    self.title = title
    self.text = None
    
class Generator():
  def __init__(self, api_key):
    self.api_key = api_key

  def generate(self) -> str:
    return str()

class OpenAIGenerator(Generator):
  def generate(self, model, **kwargs):
    headers = {"Authorization": f"Bearer {self.api_key}"}
    response = requests.post(
      "https://api.openai.com/v1/completions",
      headers=headers,
      json={"model": model, **kwargs},
    )
    r = response.json()
    try:
      return r["choices"][0]["text"]
    except:
      print(r)
   
  
# generation parameters
topic = "WW2"
author = "vilimus"
n_chapters = 3

import getpass
openai_api_key = getpass.getpass("Enter OpenAI API key: ")

gpt3 = OpenAIGenerator(openai_api_key)

# generate title
prompt = f"We are writing a book about {topic}. Generate a name for the book. Do not use quotes:\n"
title = gpt3.generate(model="text-davinci-003", prompt=prompt, max_tokens=32)
title = title.strip()

book = Book(title, author)
