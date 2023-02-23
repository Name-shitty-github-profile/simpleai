from .context import context
import openai, random
class ai:
  def __init__(self, base: str, keys: list):
    self.keys = keys
    self.base = base
    self.ctx = context(base)

  def talk(self, content: str, username: str) -> str:
    openai.api_key = random.choice(self.keys)
    self.ctx.add(username, content)
    try:
      response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(self.tx) + '\nAI : ',
        temperature=0.5,
        max_tokens=1085,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
      )["choices"][0]['text']
    except Exception as e:
      print(e)
      self.ctx.delete(-1)
      return self.get(content, username)
    self.ctx.add("AI", response)
    return response

  def add_conv(self, conv: list):
    """
    Conv structure
    A list of dicts with this structure
    ```json
    {"author": "The author of the message", "content": "The content of the message"}
    ```
    """
    for i in conv:
      self.ctx.add(i["author"], i["content"])
    return self
