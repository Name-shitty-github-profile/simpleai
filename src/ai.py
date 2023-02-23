from .context import context
import openai, random
class ai:
  def __init__(self, base: str, keys: list):
    """
    This class is a really simple class that will allows you to chat with an IA really easily
    Here's an example of code to chat with the AI in the console
    ```python
    import simpleai, os
    ai = simpleai.ai("You are a server in a bar", [os.environ["key"]])
    while True:
      content = input("Human :")
      print(ai.talk(content, "Human"))
    ```
    """
    self.keys = keys
    self.base = base
    self.ctx = context(base)

  def talk(self, content: str, username: str) -> str:
    """
    This function is for talking with the AI
    The first argument is for the content that you wanna send
    The second argument is the name of the person that says that
    Example
    ```python
    content = MyAi.talk("Hello!", "Angelica")
    print(content)
    ```
    Console
    ```
    Hello, how are you?
    ```
    """
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
      return self.talk(content, username)
    self.ctx.add("AI", response)
    return response

  def add_conv(self, conv: list):
    """
    This function is to add more data or a conversation to the AI
    Conv structure
    A list of dicts with this structure
    ```json
    {"author": "The author of the message", "content": "The content of the message"}
    ```
    """
    for i in conv:
      self.ctx.add(i["author"], i["content"])
    return self
